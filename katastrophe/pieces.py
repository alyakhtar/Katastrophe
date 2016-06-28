import math
import hashlib

from bitstring import BitArray

BLOCK_SIZE = 2**14

class Piece(object):
    def __init__(self, pieceIndex, pieceSize, pieceHash):
        self.pieceIndex = pieceIndex
        self.pieceSize = pieceSize
        self.pieceHash = pieceHash
        self.finished = False
        self.num_blocks = int(math.ceil(float(pieceSize)/BLOCK_SIZE))
        self.blockTracker = BitArray(self.num_blocks)
        self.blocks = [False]*self.num_blocks
        self.blocksSoFar = 0

    def calculateLastSize(self):
        return self.pieceSize - ((self.num_blocks-1)*(BLOCK_SIZE))

    def addBlock(self, offset, data):
        if offset == 0:
            index = 0
        else:
            index = offset/BLOCK_SIZE

        if not self.blockTracker[index]:
            self.blocks[index] = data
            self.blockTracker[index] = True
            self.blocksSoFar += 1

        self.finished = all(self.blockTracker)

        if self.finished:
            return self.checkHash()

        return True

    def reset(self):
        self.blockTracker = BitArray(self.num_blocks)
        self.finished = False

    def checkHash(self):
        allData = ''.join(self.blocks)

        hashedData = hashlib.sha1(allData).digest()
        if hashedData == self.pieceHash:
            self.block = allData
            return True
        else:
            self.piece.reset()
            return False