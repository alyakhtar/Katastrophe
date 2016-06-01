"""Katastrophe.

Usage:
  katastrophe
  katastrophe [-m | -t | -a | -s | -l | -g | -b]
  katastrophe -h | --help
  katastrophe --version

Options:
  -h, --help            Show this screen.
  --version             Show version.
  -m, --movies          Show latest Movie torrents
  -t, --tv              Show latest TV torrents
  -a, --anime           Show latest Anime torrents
  -s, --songs           Show latest Music torrents
  -l, --losslessmusic   Show latest Lossless Music torrents
  -g, --appsandgames    Show lates Application and Game Torrents
  -b, --books           Show latest Book Torrents
"""

import requests
import sys
from bs4 import BeautifulSoup
import os
import time
from tabulate import tabulate
import subprocess
from docopt import docopt
from sys import platform
from latest import movies_torrent, tv_torrent, anime_torrent, music_torrent, loslessmusic_torrent, appsndgames_torrent, books_torrent

try:
    raw_input_ = raw_input
except NameError:
    raw_input_ = input

try:
    xrange_ = xrange
except NameError:
    xrange_ = range


def print_table(serial, torrent, size, seeds, leechers):
    table = zip(serial, torrent, size, seeds, leechers)
    if not table:
        print('\nNOTHING FOUND !')
        exit()
    else:
        headers = ['S.No.', 'Torrent Name', 'Size', 'Seeders', 'Leechers']
        print(tabulate(table, headers, tablefmt='psql', numalign="center"))
        # print table


def url_generator(url, page):
    words = url.split()
    
    if len(words) == 1:
        link = 'https://kat.cr/usearch/' + words[0]
    else:
        for i in xrange_(len(words)):
            if i == 0:
                link = 'https://kat.cr/usearch/' + words[i]
            else:
                link += '%20' + words[i]
                
    if page == 1:
        return link + '/'
    return link + '/' + str(page) + '/
        
        
def fetch(url, page):

    link = url_generator(url, page)

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
    count = 0

    for name in soup.findAll('div', {'class': 'torrentname'}):
        for title in name('a', {'class': 'cellMainLink'}):
            clean_name = title.text
            new_name = ''.join([i if ord(i) < 128 else '' for i in clean_name])
            torr.append(new_name)

    for box in soup.findAll('div', {'class': 'iaconbox center floatright'}):
        count += 1
        for magnet in box('a', {'title': 'Torrent magnet link'}):
            magnet = magnet.get('href')
            mag.append(magnet)
            # print magnet
        sno.append(count)

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
    if platform == "linux" or platform == "linux2" or platform == "darwin":
        subprocess.Popen(['xdg-open', mag[torrent - 1]],
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)

    elif platform == "win32":
        procs = []
        flag = 0
        cmd = 'WMIC PROCESS get Caption'
        proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        for line in proc.stdout:
            procs.append(line.strip())

        client1 = 'bittorrent'
        client2 = 'utorrent'

        for i in procs:
            if client1 in i.lower():
                flag = 1
                break
            elif client2 in i.lower():
                flag = 2

        if flag == 1:
            cmd1 = 'wmic process where "name=\'BitTorrent.exe\'" get ExecutablePath'
            proc1 = subprocess.Popen(cmd1, shell=True, stdout=subprocess.PIPE)
            loc1 = proc1.stdout.read()
            dir1 = loc1.split('ExecutablePath')[1].strip()
            subprocess.Popen(['%s' % dir1, mag[torrent - 1]])
        elif flag == 2:
            cmd2 = 'wmic process where "name=\'uTorrent.exe\'" get ExecutablePath'
            proc2 = subprocess.Popen(cmd2, shell=True, stdout=subprocess.PIPE)
            loc2 = proc2.stdout.read()
            dir2 = loc2.split('ExecutablePath')[1].strip()
            subprocess.Popen(['%s' % dir2, mag[torrent - 1]])

        else:
            print("\nPlease Install/Run BitTorrent or uTorrent\n")


def main():
    args = docopt(__doc__, version='katastrophe 1.1.3')
    if args["--movies"]:
        movies_torrent()
    elif args["--tv"]:
        tv_torrent()
    elif args['--anime']:
        anime_torrent()
    elif args["--songs"]:
        music_torrent()
    elif args["--losslessmusic"]:
        loslessmusic_torrent()
    elif args["--appsandgames"]:
        appsndgames_torrent()
    elif args["--books"]:
        books_torrent()
    else:
        page = 1
        print("Torrent Search : "),
        query = raw_input_()
        table = fetch(query, page)

        while True:
            print('Enter torrent No. to download or m for more or b for back or e to exit : '),
            serial = raw_input_()
            if serial == 'm' or serial == 'M':
                page += 1
                fetch(query, page)
            elif serial == 'b' or serial == 'B':
                if page != 1:
                    page -= 1
                    fetch(query, page)
                else:
                    print("\n Can't Go Back !\n")
            elif serial == 'e' or serial == 'E':
                break
            else:
                download_torrent(int(serial))
                break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
    except ValueError:
        sys.exit()
