"""Katastrophe.

Usage:
  katastrophe
  katastrophe [ -m | -t | -a | -s | -l | -g | -p | -b | -x | -M | -T | -A | -S | -L | -G | -P | -B | -X ]
  katastrophe -h | --help
  katastrophe --version  

Options:
  -h, --help               Show this screen.
  --version                Show version.
  -m, --topmovies          Show top Movie torrents
  -t, --toptv              Show top TV torrents
  -a, --topanime           Show top Anime torrents
  -s, --topsongs           Show top Music torrents
  -l, --toplossless        Show top Lossless Music torrents
  -g, --topgames           Show top Game torrents
  -p, --topapplications    Show top Application torrents
  -b, --topbooks           Show top Book torrents
  -x, --topxxx             Show top XXX torrents
  -M, --movies             Search by Movie category
  -T, --tv                 Search by TV category
  -A, --anime              Search by Anime category
  -S, --songs              Search by Music category
  -L, --lossless           Search by Lossless Music category
  -G, --games              Search by Games category
  -P, --applications       Search by Applications category
  -B, --books              Search by Book category
  -X, --xxx                Search by XXX category
"""


import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
from sys import platform
import subprocess
import os
from docopt import docopt
from sys import platform


try:
    raw_input_ = raw_input
except NameError:
    raw_input_ = input

try:
    xrange_ = xrange
except NameError:
    xrange_ = range


def download_torrent(link, name):

    file_name = "".join(name.split()) # Remove whitespace from name to serve as filename.
    source_code = requests.get(link)
    plain_text = source_code.text.encode('utf-8')
    soup = BeautifulSoup(plain_text, "lxml")

    magnet = soup.find('a', {'title': 'Magnet link'}) # Extract the magnet link.
    magnet_link = magnet.get('href')

    if platform == "linux" or platform == "linux2":
        subprocess.Popen(['xdg-open', magnet_link],
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)

    elif platform == "darwin":
	            os.system('open '+magnet_link)

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
                   'deluge.exe',
                   'qbittorrent.exe']

        for c in clients:
            if c in procs:
                client = c
                break

        if client:
            cmd = 'wmic process where "name=\'{}\'" get ExecutablePath'.format(client)
            proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
            loc = proc.stdout.readlines()
            exe = loc[1].strip()
            subprocess.Popen([exe.decode(), magnet_link])
        else:
            print("Compatible torrent client not installed or running.")
            return
        
    print('Downloaded: '+name); # Let the user know which torrent was downloaded.
 

def fetch_list(media_type, query=None):

    torrent_name = []
    torrent_size = []
    torrent_seeds = []
    torrent_leechers = []
    torrent_hrefs = []
    count = 0
    link = 'https://kat.cr/'

    if query != None:
        link += 'usearch/'
        words=query.split()
        for idx,val in enumerate(words):
            if idx == 0:
                link += val
            else:
                link += '%20' + val
        if media_type != '':
            link += '%20category%3A'+media_type
    else:
        link += media_type

    source_code = requests.get(link)
    plain_text = source_code.text.encode('utf-8')
    soup = BeautifulSoup(plain_text, "lxml")

    for i in soup.findAll('table', {'class': 'data'}):
        for j in i('a', {'class': 'cellMainLink'}):
            torrent_name.append((''.join([k if ord(k) < 128 else '' for k in j.get_text()]))[:64]) # Add the torrent name - max 64 chars.
            torrent_hrefs.append(j.get('href'))
            count += 1

        for j in i('td', {'class': 'nobr center'}):
            torrent_size.append(j.get_text())

        for j in i('td', {'class': 'green center'}):
            torrent_seeds.append(j.get_text())

        for j in i('td', {'class': 'red lasttd center'}):
            torrent_leechers.append(j.get_text())

    return (count,
            list(zip(xrange_(count), torrent_name, torrent_size, torrent_seeds, torrent_leechers)),
            torrent_hrefs)


def list_torrents(media_type, query=None):
    count, torrent_list, torrent_hrefs = fetch_list(media_type, query)

    headers = ['No.', 'Name', 'Size', 'Seeds', 'Leechers']
    print('\nTop '+media_type.upper()+' torrents\n')
    print(tabulate(torrent_list, headers, tablefmt='psql', numalign="center"))

    while True:
        print('Enter torrent No.(s) to download or e to exit: '),
        req_torrents = raw_input_()
        if 'e' in req_torrents.lower():
            exit()
        else:
            if ',' in req_torrents:
                for x in req_torrents.split(','):
                    try: 
                        i = int(x)
                    except:
                        print(x+" is an invalid torrent number - ignored\n")
                        continue
                    if i >= 0 and i < count:
                        download_torrent('https://kat.cr' + torrent_hrefs[i],torrent_list[i][1])
                    else:
                        print(x+" is an invalid torrent number - ignored\n")
            else:
                try:
                    i = int(req_torrents)
                except:
                    print(req_torrents+" is an invalid torrent - ignored!\n")
                    continue
                if i >= 0 and i < count:
                    download_torrent('https://kat.cr' + torrent_hrefs[i],torrent_list[i][1])
                else:
                    print(req_torrents+" is an invalid torrent - ignored!\n")


def main():
    args = docopt(__doc__, version='katastrophe 3.0')

    media_type = '' # Set a default empty category.

    if args['--topmovies']:
        list_torrents('movies')
    elif args['--toptv']:
        list_torrents('tv')
    elif args['--topanime']:
        list_torrents('anime')
    elif args["--topsongs"]:
        list_torrents('music')
    elif args['--toplossless']:
        list_torrents('lossless')
    elif args['--topgames']:
        list_torrents('games')
    elif args["--topapplications"]:
        list_torrents('applications')
    elif args["--topbooks"]:
        list_torrents('books')
    elif args["--topxxx"]:
        list_torrents('xxx')
    elif args["--movies"]:
        media_type='movies'
    elif args["--tv"]:
        media_type='tv'
    elif args["--anime"]:
        media_type='anime'
    elif args["--songs"]:
        media_type='songs'
    elif args["--lossless"]:
        media_type='lossless'
    elif args["--books"]:
        media_type='books'
    elif args["--games"]:
        media_type='games'
    elif args["--applications"]:
        media_type='applications'
    elif args["--xxx"]:
        media_type='xxx'
        
    print("Torrent Search : "),
    query = raw_input_()
    list_torrents(media_type, query)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
    except ValueError:
        sys.exit()
