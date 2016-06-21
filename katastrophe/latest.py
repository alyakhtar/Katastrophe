import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
from sys import platform
import subprocess

try:
    raw_input_ = raw_input
except NameError:
    raw_input_ = input

try:
    xrange_ = xrange
except NameError:
    xrange_ = range


def fetch():

    link = 'https://kat.cr/full/'

    source_code = requests.get(link)

    plain_text = source_code.text.encode('utf-8')

    soup = BeautifulSoup(plain_text, "lxml")

    global movies, movies_href, tv, tv_href, anime, anime_href, music, music_href, loslessmusic
    global loslessmusic_href, appsndgames, appsndgames_href, books, books_href, headers
    movies = []
    tv = []
    appsndgames = []
    anime = []
    music = []
    loslessmusic = []
    books = []
    movies_name = []
    tv_name = []
    appsndgames_name = []
    anime_name = []
    music_name = []
    loslessmusic_name = []
    books_name = []
    movies_href = []
    tv_href = []
    appsndgames_href = []
    anime_href = []
    music_href = []
    loslessmusic_href = []
    books_href = []
    size_odd = []
    size_even = []
    seeds_odd = []
    seeds_even = []
    leechers_odd = []
    leechers_even = []
    movies_size = []
    tv_size = []
    anime_size = []
    music_size = []
    appsndgames_size = []
    loslessmusic_size = []
    books_size = []
    movies_seeds = []
    tv_seeds = []
    appsndgames_seeds = []
    anime_seeds = []
    music_seeds = []
    loslessmusic_seeds = []
    books_seeds = []
    movies_leechers = []
    tv_leechers = []
    appsndgames_leechers = []
    anime_leechers = []
    music_leechers = []
    loslessmusic_leechers = []
    books_leechers = []
    sno15 = []
    sno30 = []
    flag1 = 0
    flag2 = 0
    flag3 = 0
    flag4 = 0

    for i in soup.findAll('tr', {'class': 'odd'}):
        for j in i('div', {'class': 'markeredBlock torType filmType'}):
            for l in j('a', {'class': 'cellMainLink'}):
                flag1 += 1
                torrentname = ''.join(
                        [k if ord(k) < 128 else '' for k in l.get_text()])
                if flag1 <= 8:
                    movies_name.append(torrentname)
                    movies_href.append(l.get('href'))
                elif flag1 > 8 and flag1 <= 15:
                    tv_name.append(torrentname)
                    tv_href.append(l.get('href'))
                elif flag1 > 15 and flag1 <= 22:
                    anime_name.append(torrentname)
                    anime_href.append(l.get('href'))

        for j in i('div', {'class': 'markeredBlock torType musicType'}):
            for l in j('a', {'class': 'cellMainLink'}):
                flag2 += 1
                torrentname = ''.join(
                        [k if ord(k) < 128 else '' for k in l.get_text()])
                if flag2 <= 8:
                    music_name.append(torrentname)
                    music_href.append(l.get('href'))
                else:
                    loslessmusic_name.append(torrentname)
                    loslessmusic_href.append(l.get('href'))

        for j in i('div', {'class': 'markeredBlock torType exeType'}):
            for l in j('a', {'class': 'cellMainLink'}):
                torrentname = ''.join(
                    [k if ord(k) < 128 else '' for k in l.get_text()])
                appsndgames_name.append(torrentname)
                appsndgames_href.append(l.get('href'))

        for j in i('div', {'class': 'markeredBlock torType zipType'}):
            for l in j('a', {'class': 'cellMainLink'}):
                torrentname = ''.join(
                    [k if ord(k) < 128 else '' for k in l.get_text()])
                appsndgames_name.append(torrentname)
                appsndgames_href.append(l.get('href'))

        for j in i('div', {'class': 'markeredBlock torType pdfType'}):
            for l in j('a', {'class': 'cellMainLink'}):
                torrentname = ''.join(
                    [k if ord(k) < 128 else '' for k in l.get_text()])
                books_name.append(torrentname)
                books_href.append(l.get('href'))

    for i in soup.findAll('tr', {'class': 'even'}):
        for j in i('div', {'class': 'markeredBlock torType filmType'}):
            for l in j('a', {'class': 'cellMainLink'}):
                flag3 += 1
                torrentname = ''.join(
                        [k if ord(k) < 128 else '' for k in l.get_text()])
                if flag3 <= 7:
                    movies_name.append(torrentname)
                    movies_href.append(l.get('href'))
                elif flag3 > 7 and flag3 <= 15:
                    tv_name.append(torrentname)
                    tv_href.append(l.get('href'))
                elif flag3 > 15 and flag3 <= 23:
                    anime_name.append(torrentname)
                    anime_href.append(l.get('href'))

        for j in i('div', {'class': 'markeredBlock torType musicType'}):
            for l in j('a', {'class': 'cellMainLink'}):
                flag4 += 1
                torrentname = ''.join(
                        [k if ord(k) < 128 else '' for k in l.get_text()])
                if flag4 <= 7:
                    music_name.append(torrentname)
                    music_href.append(l.get('href'))
                else:
                    loslessmusic_name.append(torrentname)
                    loslessmusic_href.append(l.get('href'))

        for j in i('div', {'class': 'markeredBlock torType exeType'}):
            for l in j('a', {'class': 'cellMainLink'}):
                torrentname = ''.join(
                    [k if ord(k) < 128 else '' for k in l.get_text()])
                appsndgames_name.append(torrentname)
                appsndgames_href.append(l.get('href'))

        for j in i('div', {'class': 'markeredBlock torType zipType'}):
            for l in j('a', {'class': 'cellMainLink'}):
                torrentname = ''.join(
                    [k if ord(k) < 128 else '' for k in l.get_text()])
                appsndgames_name.append(torrentname)
                appsndgames_href.append(l.get('href'))

        for j in i('div', {'class': 'markeredBlock torType pdfType'}):
            for l in j('a', {'class': 'cellMainLink'}):
                torrentname = ''.join(
                    [k if ord(k) < 128 else '' for k in l.get_text()])
                books_name.append(torrentname)
                books_href.append(l.get('href'))

    for i in soup.findAll('tr', {'class': 'odd'}):
        for j in i('td', {'class': 'nobr center'}):
            size_odd.append(j.get_text())

        for j in i('td', {'class': 'green center'}):
            seeds_odd.append(j.get_text())

        for j in i('td', {'class': 'red lasttd center'}):
            leechers_odd.append(j.get_text())

    for i in soup.findAll('tr', {'class': 'even'}):
        for j in i('td', {'class': 'nobr center'}):
            size_even.append(j.get_text())

        for j in i('td', {'class': 'green center'}):
            seeds_even.append(j.get_text())

        for j in i('td', {'class': 'red lasttd center'}):
            leechers_even.append(j.get_text())

    for i in xrange_(60):
        if i < 8:
            movies_size.append(size_odd[i])
            movies_seeds.append(seeds_odd[i])
            movies_leechers.append(leechers_odd[i])
            sno15.append(i + 1)
            sno30.append(i + 1)
        elif i >= 8 and i < 15:
            tv_size.append(size_odd[i])
            tv_seeds.append(seeds_odd[i])
            tv_leechers.append(leechers_odd[i])
            sno15.append(i + 1)
            sno30.append(i + 1)
        elif i >= 15 and i < 22:
            anime_size.append(size_odd[i])
            anime_seeds.append(seeds_odd[i])
            anime_leechers.append(leechers_odd[i])
            sno30.append(i + 1)
        elif i >= 22 and i < 30:
            music_size.append(size_odd[i])
            music_seeds.append(seeds_odd[i])
            music_leechers.append(leechers_odd[i])
            sno30.append(i + 1)
        elif i >= 30 and i < 37:
            loslessmusic_size.append(size_odd[i])
            loslessmusic_seeds.append(seeds_odd[i])
            loslessmusic_leechers.append(leechers_odd[i])
        elif i >= 37 and i < 52:
            appsndgames_size.append(size_odd[i])
            appsndgames_seeds.append(seeds_odd[i])
            appsndgames_leechers.append(leechers_odd[i])
        else:
            books_size.append(size_odd[i])
            books_seeds.append(seeds_odd[i])
            books_leechers.append(leechers_odd[i])

    for i in xrange_(60):
        if i < 7:
            movies_size.append(size_even[i])
            movies_seeds.append(seeds_even[i])
            movies_leechers.append(leechers_even[i])
        elif i >= 7 and i < 15:
            tv_size.append(size_even[i])
            tv_seeds.append(seeds_even[i])
            tv_leechers.append(leechers_even[i])
        elif i >= 15 and i < 23:
            anime_size.append(size_even[i])
            anime_seeds.append(seeds_even[i])
            anime_leechers.append(leechers_even[i])
        elif i >= 23 and i < 30:
            music_size.append(size_even[i])
            music_seeds.append(seeds_even[i])
            music_leechers.append(leechers_even[i])
        elif i >= 30 and i < 38:
            loslessmusic_size.append(size_even[i])
            loslessmusic_seeds.append(seeds_even[i])
            loslessmusic_leechers.append(leechers_even[i])
        elif i >= 38 and i < 53:
            appsndgames_size.append(size_even[i])
            appsndgames_seeds.append(seeds_even[i])
            appsndgames_leechers.append(leechers_even[i])
        else:
            books_size.append(size_even[i])
            books_seeds.append(seeds_even[i])
            books_leechers.append(leechers_even[i])

    headers = ['SNO.', 'NAME', 'SIZE', 'SEEDS', 'LEECHERS']
    movies = zip(sno15, movies_name, movies_size, movies_seeds,
                 movies_leechers)
    tv = zip(sno15, tv_name, tv_size, tv_seeds, tv_leechers)
    anime = zip(sno15, anime_name, anime_size, anime_seeds, anime_leechers)
    music = zip(sno15, music_name, music_size, music_seeds, music_leechers)
    loslessmusic = zip(sno15, loslessmusic_name, loslessmusic_size,
                       loslessmusic_seeds, loslessmusic_leechers)
    appsndgames = zip(sno30, appsndgames_name, appsndgames_size,
                      appsndgames_seeds, appsndgames_leechers)
    books = zip(sno15, books_name, books_size, books_seeds, books_leechers)


def download_torrent(link):
    source_code = requests.get(link)

    plain_text = source_code.text.encode('utf-8')

    soup = BeautifulSoup(plain_text, "lxml")

    magnet = soup.find('a', {'title': 'Magnet link'})
    magnet_link = magnet.get('href')

    if platform == "linux" or platform == "linux2":
        subprocess.Popen(['xdg-open', magnet_link],
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)

    elif platform == "darwin":
        subprocess.Popen(['xdg-open', magnet_link],
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)

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
            subprocess.Popen([exe.decode(), magnet_link])
        else:
            print("\nPlease Install/Run BitTorrent, uTorrent, or deluge.\n")


def movies_torrent():
    fetch()
    print(tabulate(movies, headers, tablefmt='psql', numalign="center"))
    print('Enter torrent No.(s) to download or e to exit : '),
    serial = raw_input_()
    if serial == 'e' or serial == 'E':
        exit()
    else:
        if ',' in serial:
            numbs = serial.split(',')
            if len(numbs) < 3:
                if numbs[0] != '' and numbs[1] != '' :
                    start = int(numbs[0])
                    end = int(numbs[1])
                    if start < end:
                        if end < 16 and start > 0:
                            for i in xrange(start,end+1):
                                download_torrent('https://kat.cr' + movies_href[i - 1])
                elif numbs[0] != '' and numbs[1] == '' :
                    start = int(numbs[0])
                    if start > 0 and start < 16:
                        for i in xrange(start,16):
                            download_torrent('https://kat.cr' + movies_href[i - 1])
                else:
                    end = int(numbs[1])
                    if end > 0 and end < 16:
                        for i in xrange(1,end+1):
                            download_torrent('https://kat.cr' + movies_href[i - 1])
            else:
                for sn in numbs:
                    i = int(sn)
                    if i > 0 and i < 16:
                        download_torrent('https://kat.cr' + movies_href[i - 1])
                    else:
                        print "\n\n\tINCORRECT SERIAL NUMBERS!!\n\n"

        else:
            if int(serial) <= 15 and int(serial) >= 1: 
                download_torrent('https://kat.cr' + movies_href[int(serial) - 1])
            else:
                print "\n\n\tINCORRECT SERIAL, TORRRENT DOES NOT EXIST!!\n\n"


def tv_torrent():
    fetch()
    print(tabulate(tv, headers, tablefmt='psql', numalign="center"))
    print('Enter torrent No.(s) to download or e to exit : '),
    serial = raw_input_()
    if serial == 'e' or serial == 'E':
        exit()
    else:
        if ',' in serial:
            numbs = serial.split(',')
            if len(numbs) < 3:
                if numbs[0] != '' and numbs[1] != '' :
                    start = int(numbs[0])
                    end = int(numbs[1])
                    if start < end:
                        if end < 16 and start > 0:
                            for i in xrange(start,end+1):
                                download_torrent('https://kat.cr' + tv_href[i - 1])
                elif numbs[0] != '' and numbs[1] == '' :
                    start = int(numbs[0])
                    if start > 0 and start < 16:
                        for i in xrange(start,16):
                            download_torrent('https://kat.cr' + tv_href[i - 1])
                else:
                    end = int(numbs[1])
                    if end > 0 and end < 16:
                        for i in xrange(1,end+1):
                            download_torrent('https://kat.cr' + tv_href[i - 1])
            else:
                for sn in numbs:
                    i = int(sn)
                    if i > 0 and i < 16:
                        download_torrent('https://kat.cr' + tv_href[i - 1])
                    else:
                        print "\n\n\tINCORRECT SERIAL NUMBERS!!\n\n"

        else:
            if int(serial) <= 15 and int(serial) >= 1: 
                download_torrent('https://kat.cr' + tv_href[int(serial) - 1])
            else:
                print "\n\n\tINCORRECT SERIAL, TORRRENT DOES NOT EXIST!!\n\n"


def anime_torrent():
    fetch()
    print(tabulate(anime, headers, tablefmt='psql', numalign="center"))
    print('Enter torrent No.(s) to download or e to exit : '),
    serial = raw_input_()
    if serial == 'e' or serial == 'E':
        exit()
    else:
        if ',' in serial:
            numbs = serial.split(',')
            if len(numbs) < 3:
                if numbs[0] != '' and numbs[1] != '' :
                    start = int(numbs[0])
                    end = int(numbs[1])
                    if start < end:
                        if end < 16 and start > 0:
                            for i in xrange(start,end+1):
                                download_torrent('https://kat.cr' + anime_href[i - 1])
                elif numbs[0] != '' and numbs[1] == '' :
                    start = int(numbs[0])
                    if start > 0 and start < 16:
                        for i in xrange(start,16):
                            download_torrent('https://kat.cr' + anime_href[i - 1])
                else:
                    end = int(numbs[1])
                    if end > 0 and end < 16:
                        for i in xrange(1,end+1):
                            download_torrent('https://kat.cr' + anime_href[i - 1])
            else:
                for sn in numbs:
                    i = int(sn)
                    if i > 0 and i < 16:
                        download_torrent('https://kat.cr' + anime_href[i - 1])
                    else:
                        print "\n\n\tINCORRECT SERIAL NUMBERS!!\n\n"

        else:
            if int(serial) <= 15 and int(serial) >= 1: 
                download_torrent('https://kat.cr' + anime_href[int(serial) - 1])
            else:
                print "\n\n\tINCORRECT SERIAL, TORRRENT DOES NOT EXIST!!\n\n"


def music_torrent():
    fetch()
    print(tabulate(music, headers, tablefmt='psql', numalign="center"))
    print('Enter torrent No.(s) to download or e to exit : '),
    serial = raw_input_()
    if serial == 'e' or serial == 'E':
        exit()
    else:
        if ',' in serial:
            numbs = serial.split(',')
            if len(numbs) < 3:
                if numbs[0] != '' and numbs[1] != '' :
                    start = int(numbs[0])
                    end = int(numbs[1])
                    if start < end:
                        if end < 16 and start > 0:
                            for i in xrange(start,end+1):
                                download_torrent('https://kat.cr' + music_href[i - 1])
                elif numbs[0] != '' and numbs[1] == '' :
                    start = int(numbs[0])
                    if start > 0 and start < 16:
                        for i in xrange(start,16):
                            download_torrent('https://kat.cr' + music_href[i - 1])
                else:
                    end = int(numbs[1])
                    if end > 0 and end < 16:
                        for i in xrange(1,end+1):
                            download_torrent('https://kat.cr' + music_href[i - 1])
            else:
                for sn in numbs:
                    i = int(sn)
                    if i > 0 and i < 16:
                        download_torrent('https://kat.cr' + music_href[i - 1])
                    else:
                        print "\n\n\tINCORRECT SERIAL NUMBERS!!\n\n"

        else:
            if int(serial) <= 15 and int(serial) >= 1: 
                download_torrent('https://kat.cr' + music_href[int(serial) - 1])
            else:
                print "\n\n\tINCORRECT SERIAL, TORRRENT DOES NOT EXIST!!\n\n"


def loslessmusic_torrent():
    fetch()
    print(tabulate(loslessmusic, headers, tablefmt='psql', numalign="center"))
    print('Enter torrent No.(s) to download or e to exit : '),
    serial = raw_input_()
    if serial == 'e' or serial == 'E':
        exit()
    else:
        if ',' in serial:
            numbs = serial.split(',')
            if len(numbs) < 3:
                if numbs[0] != '' and numbs[1] != '' :
                    start = int(numbs[0])
                    end = int(numbs[1])
                    if start < end:
                        if end < 16 and start > 0:
                            for i in xrange(start,end+1):
                                download_torrent('https://kat.cr' + loslessmusic_href[i - 1])
                elif numbs[0] != '' and numbs[1] == '' :
                    start = int(numbs[0])
                    if start > 0 and start < 16:
                        for i in xrange(start,16):
                            download_torrent('https://kat.cr' + loslessmusic_href[i - 1])
                else:
                    end = int(numbs[1])
                    if end > 0 and end < 16:
                        for i in xrange(1,end+1):
                            download_torrent('https://kat.cr' + loslessmusic_href[i - 1])
            else:
                for sn in numbs:
                    i = int(sn)
                    if i > 0 and i < 16:
                        download_torrent('https://kat.cr' + loslessmusic_href[i - 1])
                    else:
                        print "\n\n\tINCORRECT SERIAL NUMBERS!!\n\n"

        else:
            if int(serial) <= 15 and int(serial) >= 1: 
                download_torrent('https://kat.cr' + loslessmusic_href[int(serial) - 1])
            else:
                print "\n\n\tINCORRECT SERIAL, TORRRENT DOES NOT EXIST!!\n\n"


def appsndgames_torrent():
    fetch()
    print(tabulate(appsndgames, headers, tablefmt='psql', numalign="center"))
    print('Enter torrent No.(s) to download or e to exit : '),
    serial = raw_input_()
    if serial == 'e' or serial == 'E':
        exit()
    else:
        if ',' in serial:
            numbs = serial.split(',')
            if len(numbs) < 3:
                if numbs[0] != '' and numbs[1] != '' :
                    start = int(numbs[0])
                    end = int(numbs[1])
                    if start < end:
                        if end < 31 and start > 0:
                            for i in xrange(start,end+1):
                                download_torrent('https://kat.cr' + appsndgames_href[i - 1])
                elif numbs[0] != '' and numbs[1] == '' :
                    start = int(numbs[0])
                    if start > 0 and start < 31:
                        for i in xrange(start,31):
                            download_torrent('https://kat.cr' + appsndgames_href[i - 1])
                else:
                    end = int(numbs[1])
                    if end > 0 and end < 31:
                        for i in xrange(1,end+1):
                            download_torrent('https://kat.cr' + appsndgames_href[i - 1])
            else:
                for sn in numbs:
                    i = int(sn)
                    if i > 0 and i < 31:
                        download_torrent('https://kat.cr' + appsndgames_href[i - 1])
                    else:
                        print "\n\n\tINCORRECT SERIAL NUMBERS!!\n\n"

        else:
            if int(serial) <= 30 and int(serial) >= 1: 
                download_torrent('https://kat.cr' + appsndgames_href[int(serial) - 1])
            else:
                print "\n\n\tINCORRECT SERIAL, TORRRENT DOES NOT EXIST!!\n\n"


def books_torrent():
    fetch()
    print(tabulate(books, headers, tablefmt='psql', numalign="center"))
    print('Enter torrent No.(s) to download or e to exit : '),
    serial = raw_input_()
    if serial == 'e' or serial == 'E':
        exit()
    else:
        if ',' in serial:
            numbs = serial.split(',')
            if len(numbs) < 3:
                if numbs[0] != '' and numbs[1] != '' :
                    start = int(numbs[0])
                    end = int(numbs[1])
                    if start < end:
                        if end < 16 and start > 0:
                            for i in xrange(start,end+1):
                                download_torrent('https://kat.cr' + books_href[i - 1])
                elif numbs[0] != '' and numbs[1] == '' :
                    start = int(numbs[0])
                    if start > 0 and start < 16:
                        for i in xrange(start,16):
                            download_torrent('https://kat.cr' + books_href[i - 1])
                else:
                    end = int(numbs[1])
                    if end > 0 and end < 16:
                        for i in xrange(1,end+1):
                            download_torrent('https://kat.cr' + books_href[i - 1])
            else:
                for sn in numbs:
                    i = int(sn)
                    if i > 0 and i < 16:
                        download_torrent('https://kat.cr' + books_href[i - 1])
                    else:
                        print "\n\n\tINCORRECT SERIAL NUMBERS!!\n\n"

        else:
            if int(serial) <= 15 and int(serial) >= 1: 
                download_torrent('https://kat.cr' + books_href[int(serial) - 1])
            else:
                print "\n\n\tINCORRECT SERIAL, TORRRENT DOES NOT EXIST!!\n\n"