import sys
from sys import platform
from peers import PeerManager
from reactor import Reactor
import Queue
import getpass


def download(name):
    shared_mem = Queue.PriorityQueue()
    user = getpass.getuser()
    if platform == "win32":
    	directory = 'C:\Users' + user + '\Torrents\\'
    else:
    	directory = '/home/'+ user +'/Torrents/'
    Torrent = directory + name
    peerMngr = PeerManager(Torrent)
    bittorrentThread = Reactor(1, "Thread-1", peerMngr, shared_mem, debug=True)
    bittorrentThread.run()