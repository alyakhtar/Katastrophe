import hashlib
import socket
import math
from collections import deque
import logging
import sys
import bencode
from bitstring import BitArray

import pieces
import scrape

# logging = logging.getLogger('Peer_Manager')

class PeerManager(object):

    def __init__(self, trackerFile):
        self.peer_id = '0987654321098765432-'
        self.peers = []
        self.pieces = deque([])
        self.tracker = bencode.bdecode(open(trackerFile,'rb').read())
        bencodeInfo = bencode.bencode(self.tracker['info'])
        self.infoHash = hashlib.sha1(bencodeInfo).digest()
        self.getPeers()
        self.generatePieces()
        self.numPiecesSoFar = 0

    def generatePieces(self):
        logging.info("Initalizing... ")
        pieceHashes = self.tracker['info']['pieces']
        pieceLength = self.tracker['info']['piece length']
        if 'files' in self.tracker['info']:
            files = self.tracker['info']['files']
            totalLength = sum([file['length'] for file in files])
            self.numPieces =  int(math.ceil(float(totalLength)/pieceLength))
        else:
            totalLength = self.tracker['info']['length']
            self.numPieces = int(math.ceil(float(totalLength)/pieceLength))

        counter = totalLength
        self.totalLength = totalLength
        for i in range(self.numPieces):
            if i == self.numPieces-1:
                self.pieces.append(pieces.Piece(i, counter, pieceHashes[0:20]))
            else:
                self.pieces.append(pieces.Piece(i, pieceLength, pieceHashes[0:20]))
                counter -= pieceLength
                pieceHashes = pieceHashes[20:]

        self.curPiece = self.pieces.popleft()

    def chunkToSixBytes(self, peerString):
        for i in xrange(0, len(peerString), 6):
            chunk = peerString[i:i+6]
            if len(chunk) < 6:
                import pudb; pudb.set_trace()
                raise IndexError("Size of the chunk was not six bytes.")
            yield chunk

    def findHTTPServer(self):
        annouceList = self.tracker['announce-list']
        return [x[0] for x in annouceList if x[0].startswith('http')]

    def getPeers(self):
        announce_list = []
        if 'announce-list' in self.tracker:
            announce_list = self.tracker['announce-list']
        else:
            announce_list.append([self.tracker['announce']])
        for announce in announce_list:
            announce = announce[0]
            if announce.startswith('http'):
                length = str(self.tracker['info']['piece length'])
                response = scrape.scrape_http(announce, self.infoHash, self.peer_id, length)
            elif announce.startswith('udp'):
                response = scrape.scrape_udp(self.infoHash, announce, self.peer_id)
            if response:
                break
        for chunk in self.chunkToSixBytes(response):
            ip = []
            port = None
            for i in range(0, 4):
                ip.append(str(ord(chunk[i])))

            port = ord(chunk[4])*256+ord(chunk[5])
            mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            mySocket.setblocking(0)
            ip = '.'.join(ip)
            peer = Peer(ip, port, mySocket, self.infoHash, self.peer_id)
            self.peers.append(peer)

    def findNextBlock(self, peer):
        for blockIndex in range(self.curPiece.num_blocks):
            if not self.curPiece.blockTracker[blockIndex]:
                if blockIndex == self.curPiece.num_blocks-1:
                    size = self.curPiece.calculateLastSize()
                else:
                    size = pieces.BLOCK_SIZE
                return (self.curPiece.pieceIndex, 
                        blockIndex*pieces.BLOCK_SIZE,
                        size)
        return None

    def checkIfDoneDownloading(self):
        now = self.numPiecesSoFar
        final = self.numPieces
        newfinal = 100
        NewValue = now

        if final != 100:
            OldRange = final  
            NewRange = 100  
            NewValue = ((now * NewRange) / OldRange)

        percentage = (float(NewValue)/float(newfinal)) * 100
        sys.stdout.write("\r[%s>%s] %d%% Completed" % ('=' * (NewValue),' ' * (newfinal - NewValue),percentage))
        return now == final
        sys.stdout.flush()

class Peer(object):
    def __init__(self, ip, port, socket, infoHash, peer_id):
        self.ip = ip
        self.port = port
        self.choked = False
        self.bitField = None
        self.sentInterested = False
        self.socket = socket
        self.bufferWrite = self.makeHandshakeMsg(infoHash, peer_id)
        self.bufferRead = ''
        self.handshake = False

    def makeHandshakeMsg(self, infoHash, peer_id):
        pstrlen = '\x13'
        pstr = 'BitTorrent protocol'
        reserved = '\x00\x00\x00\x00\x00\x00\x00\x00'
       
        handshake = pstrlen+pstr+reserved+infoHash+peer_id

        return handshake

    def setBitField(self, payload):
        self.bitField = BitArray(bytes=payload)

    def fileno(self):
        return self.socket.fileno()

class HTTPObj(object):
    def __init__(self):
        pass

    def onProcess(self):
        pass
    def fileno(self):
        pass 
