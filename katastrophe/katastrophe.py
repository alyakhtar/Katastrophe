import requests
import sys
from bs4 import BeautifulSoup
import os
import time
from tabulate import tabulate
import subprocess
from sys import platform


def print_table(serial, torrent, size, seeds, leechers):
    table = zip(serial, torrent, size, seeds, leechers)
    if not table:
        print '\nNOTHING FOUND !'
        exit()
    else:
        headers = ['S.No.', 'Torrent Name', 'Size', 'Seeders', 'Leechers']
        print tabulate(table, headers, tablefmt='psql', numalign="center")
        # print table


def url_generetor(url, page):
    words = url.split()
    if page == 1:
        if len(words) == 1:
            link = 'https://kat.cr/usearch/'+words[0]
        else:
            for i in xrange(len(words)):
                if i == 0:
                    link = 'https://kat.cr/usearch/'+words[i]
                else:
                    link += '%20'+words[i]

        return link+'/'

    else:
        if len(words) == 1:
            link = 'https://kat.cr/usearch/'+words[0]
        else:
            for i in xrange(len(words)):
                if i == 0:
                    link = 'https://kat.cr/usearch/'+words[i]
                else:
                    link += '%20'+words[i]

        return link + '/' + str(page) + '/'


def fetch(url, page):

    link = url_generetor(url, page)

    source_code = requests.get(link)

    plain_text = source_code.text.encode('utf-8')

    soup = BeautifulSoup(plain_text, "lxml")
    # soup = soup.encode("utf-8")

    global mag
    torr = []
    mag = []
    sd = []
    lc = []
    sz = []
    mytable = []
    sno = []
    i = 0

    for name in soup.findAll('div', {'class': 'torrentname'}):
        for title in name('a', {'class': 'cellMainLink'}):
            clean_name = title.text
            torr.append(clean_name.encode("utf-8"))

    for box in soup.findAll('div', {'class': 'iaconbox center floatright'}):
        i += 1
        for magnet in box('a', {'title': 'Torrent magnet link'}):
            magnet = magnet.get('href')
            mag.append(magnet)
            # print magnet
        sno.append(i)

    for space in soup.findAll('td', {'class': 'nobr center'}):
        size = space.get_text()
        sz.append(size)
        # print size

    for seed in soup.findAll('td', {'class': 'green center'}):
        seeds = seed.get_text()
        sd.append(seeds)
        # print seeds

    for leech in soup.findAll('td', {'class': 'red lasttd center'}):
        leechers = leech.get_text()
        lc.append(leechers)
        # print leechers

    print_table(sno, torr, sz, sd, lc)


def download_torrent(torrent):
    if platform == "linux" or platform == "linux2":
        subprocess.Popen(
            ['xdg-open', mag[torrent-1]], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    elif platform == "darwin":
        subprocess.Popen(
            ['xdg-open', mag[torrent-1]], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    elif platform == "win32":
        if os.path.exists("C:\Users\Aly Akhtar\AppData\Roaming\uTorrent\uTorrent.exe"):
            subprocess.Popen(['C:\Users\Aly Akhtar\AppData\Roaming\uTorrent\uTorrent.exe', mag[torrent-1]])
        elif os.path.exists("C:\Users\Aly Akhtar\AppData\Roaming\BitTorrent\BitTorrent.exe"):
            subprocess.Popen(['C:\Users\Aly Akhtar\AppData\Roaming\BitTorrent\BitTorrent.exe', mag[torrent-1]])


def main():
    page = 1
    start = time.time()
    print "Torrent Search : ",
    query = raw_input()
    table = fetch(query, page)

    while True:
        print 'Enter torrent No. to download or m for more or b for back or e to exit : ',
        serial = raw_input()
        if serial == 'm' or serial == 'M':
            page += 1
            fetch(query, page)
        elif serial == 'b' or serial == 'B':
            if page != 1:
                page -= 1
                fetch(query, page)
            else:
                print "\n Can't Go Back !\n"
        elif serial == 'e' or serial == 'E':
            break
        else:
            download_torrent(int(serial))
            break

    end = time.time()
    # print '\nTime Taken : ', end - start, 'seconds'

if __name__ == "__main__":
    main()
