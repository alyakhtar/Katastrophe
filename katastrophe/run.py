import sys
from peers import PeerManager
from reactor import Reactor
import Queue


def download(name):
    shared_mem = Queue.PriorityQueue()
    Torrent = '../Torrents/'+name
    peerMngr = PeerManager(Torrent)
    bittorrentThread = Reactor(1, "Thread-1", peerMngr, shared_mem, debug=True)
    bittorrentThread.run()