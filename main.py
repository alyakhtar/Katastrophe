import requests
import sys
from bs4 import BeautifulSoup
import os
import time
from tabulate import tabulate
import subprocess


def url_generetor(url):
    words = url.split()
    if len(words) == 1:
        link = 'https://kat.cr/usearch/'+words[0]+'/'
    else:
        for i in xrange(len(words)):
            if  i == 0:
                link = 'https://kat.cr/usearch/'+words[i]
            else:
                link += '%20'+words[i]

    return link+'/'


def fetch(url):

    link = url_generetor(url)

    source_code = requests.get(link)

    plain_text = source_code.text.encode('utf-8')

    soup = BeautifulSoup(plain_text, "lxml")

    torr = []
    mag = []
    sd = []
    lc = []
    sz = []
    mytable = []
    sno = []
    i = 0

    for box in soup.findAll('div', {'class': 'iaconbox center floatright'}):
        i += 1
        for title in box('a',{'class':'icommentjs kaButton smallButton rightButton'}):
            # print title.get('href')
            comment = title.get('href')
            comment_clean = comment.split('/')
            name = ''.join(comment[1:])
            name_clean = name.split('.')
            # print name_clean[0]
            torr.append(name_clean[0])
        for magnet in box('a',{'title':'Torrent magnet link'}):
            magnet = magnet.get('href')
            mag.append(magnet)
            # print magnet
        sno.append(i)

    for space in soup.findAll('td',{'class':'nobr center'}):
        size = space.get_text()
        sz.append(size)
        # print size

    for seed in soup.findAll('td',{'class':'green center'}):
        seeds = seed.get_text()
        sd.append(seeds)
        # print seeds

    for leech in soup.findAll('td',{'class':'red lasttd center'}):
        leechers = leech.get_text()
        lc.append(leechers)
        # print leechers

    mytable = zip(sno,torr,sz,sd,lc)
    headers = ['S.No.','Torrent Name','Size','Seeders','Leechers']
    print tabulate(mytable,headers,tablefmt='psql',numalign="center")

    print 'Enter torrent No. to download : ',
    serial = int(raw_input())

    # print serial
    print mag[serial-1]

    # os.startfile('C:\Users\Aly Akhtar\AppData\Roaming\BitTorrent\BitTorrent.exe')
    subprocess.Popen(['xdg-open', mag[serial-1]+'.torrent'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # if i == 37:
    #     done = 98

    # sys.stdout.write("\r[%s%s] %d%% Completed" %
    #                  ('=' * i, ' ' * (38 - i), done))
    # done = done + 2.63
    # i += 1

    # sys.stdout.flush()

# def download_torrent():



if __name__ == "__main__":
    start = time.time()
    print "Enter Search field : ",
    url = raw_input()
    fetch(url)
    end = time.time()
    print '\nTime Taken : ', end - start, 'seconds'

