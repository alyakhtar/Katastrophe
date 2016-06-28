"""Katastrophe.

Usage:
  katastrophe
  katastrophe [-m | -t | -a | -s | -l | -g | -p | -b | -x | -M | -T | -A | -S | -B | -G | -P | -X]
  katastrophe -h | --help
  katastrophe --version  
  Multi Download:
    i,j     From Serial No. i to Serial No. j
    ,i      From Serial No. 1 to Serial No. i 
    i,      From Serial No. i to serial no 25
    i,j,... Multiple Serial Numbers


Options:
  -h, --help               Show this screen.
  --version                Show version.
  -m, --newmovies          Show latest Movie torrents
  -t, --newtv              Show latest TV torrents
  -a, --newanime           Show latest Anime torrents
  -s, --newsongs           Show latest Music torrents
  -l, --newlosslessmusic   Show latest Lossless Music torrents
  -g, --newgames           Show lates Game Torrents
  -p, --newapplications    Show latest Application Torrents
  -b, --newbooks           Show latest Book Torrents
  -x, --xxx                Show latest XXX Torrents
  -M, --movies             Search by Movie Category
  -T, --tv                 Search by TV Category
  -A, --anime              Search by Anime Category
  -S, --songs              Search by Music Category
  -B, --books              Search by Book Category
  -G, --games              Search by Games Category
  -P, --applications       Search by Applications Category
  -X, --XXX                Search by XXX Category
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
from latest import movies_torrent, tv_torrent, anime_torrent, music_torrent, losslessmusic_torrent, applications_torrent, books_torrent,games_torrent
from subcategories import categories,xxx_torrent
# from run import download

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
        print('\n\tNOTHING FOUND !')
        exit()
    else:
        headers = ['S.No.', 'Torrent Name', 'Size', 'Seeders', 'Leechers']
        print(tabulate(table, headers, tablefmt='psql', numalign="center"))


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
    return link + '/' + str(page) + '/'
        
        
def fetch(url, page):

    link = url_generator(url, page)

    source_code = requests.get(link)

    plain_text = source_code.text.encode('utf-8')

    soup = BeautifulSoup(plain_text, "lxml")

    global mag
    global torr_file
    global torr
    torr_file = []
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
        for file in box('a',{'title':'Download torrent file'}):
            torr_name = 'https:'+file.get('href')
            torr_file.append(torr_name)
        sno.append(count)

    for space in soup.findAll('td', {'class': 'nobr center'}):
        size = space.get_text()
        sz.append(size)

    for seed in soup.findAll('td', {'class': 'green center'}):
        seeds = seed.get_text()
        sd.append(seeds)

    for leech in soup.findAll('td', {'class': 'red lasttd center'}):
        leechers = leech.get_text()
        lc.append(leechers)

    print_table(sno, torr, sz, sd, lc)


def download_torrent(torrent):
    file_name = "".join(torr[torrent-1].split())
    
    if platform == "linux" or platform == "linux2":
        subprocess.Popen(['xdg-open', mag[torrent - 1]],
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    elif platform == "darwin":
        os.system('open '+mag[torrent - 1])

    elif platform == "win32":
        procs = []
        flag = 0
        client = ''
        cmd = 'WMIC PROCESS get Caption'
        proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        for line in proc.stdout:
            procs.append(line.strip())

        clients = ['BitTorrent.exe',
                   'uTorrent.exe',
                   'deluge.exe']

        for c in clients:
            if c in procs:
                client = c
                break
    
        if client:
            cmd = 'wmic process where "name=\'{}\'" get ExecutablePath'.format(client)
            proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
            loc = proc.stdout.readlines()
            exe = loc[1].strip()
            subprocess.Popen([exe.decode(), mag[torrent - 1]])
        else:
            print("\nPlease Install/Run BitTorrent, uTorrent, or deluge.\n")
        # pwrshell = subprocess.Popen([r'C:\WINDOWS\system32\WindowsPowerShell\v1.0\powershell.exe',
        #                  '-ExecutionPolicy',
        #                  'Unrestricted',
        #                  'wget %s -Outfile ../Torrents/%s.torrent' %(torr_file[torrent-1],file_name)], cwd=os.getcwd())
        # result = pwrshell.wait()
        # download(file_name+'.torrent')


def main():
    args = docopt(__doc__, version='katastrophe 1.1.9')
    if args["--newmovies"]:
        movies_torrent()
    elif args["--newtv"]:
        tv_torrent()
    elif args['--newanime']:
        anime_torrent()
    elif args["--newsongs"]:
        music_torrent()
    elif args["--newlosslessmusic"]:
        losslessmusic_torrent()
    elif args["--newgames"]:
        games_torrent()
    elif args["--newapplications"]:
        applications_torrent()
    elif args["--newbooks"]:
        books_torrent()
    elif args["--xxx"]:
        xxx_torrent()
    elif args["--movies"]:
        categories(0)
    elif args["--tv"]:
        categories(1)
    elif args["--anime"]:
        categories(2)
    elif args["--songs"]:
        categories(3)
    elif args["--books"]:
        categories(4)
    elif args["--games"]:
        categories(5)
    elif args["--applications"]:
        categories(6)
    elif args["--XXX"]:
        categories(7)
    else:
        page = 1
        print("Torrent Search : "),
        query = raw_input_()
        table = fetch(query, page)

        while True:
            print('Enter torrent No.(s) to download or m for more or b for back or e to exit : '),
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
                if ',' in serial:
                    numbs = serial.split(',')
                    if len(numbs) < 3:
                        if numbs[0] != '' and numbs[1] != '' :
                            start = int(numbs[0])
                            end = int(numbs[1])
                            if start < end:
                                if end < 26 and start > 0:
                                    for i in xrange(start,end+1):
                                        download_torrent(i)
                            break
                        elif numbs[0] != '' and numbs[1] == '' :
                            start = int(numbs[0])
                            if start > 0 and start < 26:
                                for i in xrange(start,26):
                                    download_torrent(i)
                            break
                        else:
                            end = int(numbs[1])
                            if end > 0 and end < 26:
                                for i in xrange(1,end+1):
                                    download_torrent(i)
                            break
                    else:
                        for sn in numbs:
                            i = int(sn)
                            if i > 0 and i < 26:
                                download_torrent(i)
                            else:
                                print("\n\n\tINCORRECT SERIAL NUMBERS!!\n\n")
                        break

                else:
                    if int(serial) <= 25 and int(serial) >= 1: 
                        download_torrent(int(serial))
                        break
                    else:
                        print("\n\n\tINCORRECT SERIAL, TORRRENT DOES NOT EXIST!!\n\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
    except ValueError:
        sys.exit()
