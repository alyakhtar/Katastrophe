import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
from sys import platform
import subprocess
import os,time
from run import download
import getpass

try:
    raw_input_ = raw_input
except NameError:
    raw_input_ = input

try:
    xrange_ = xrange
except NameError:
    xrange_ = range


def download_torrent(link, name):
    file_name = "".join(name.split())

    source_code = requests.get(link)

    plain_text = source_code.text.encode('utf-8')

    soup = BeautifulSoup(plain_text, "lxml")

    magnet = soup.find('a', {'title': 'Magnet link'})
    magnet_link = magnet.get('href')
    torr = soup.find('a', {'title': 'Download verified torrent file'})
    torr_file = torr.get('href')

    user = getpass.getuser()

    directory = 'Torrents'

    if platform == "linux" or platform == "linux2" or platform == "darwin":
        directory = '/home/'+ user +'/Torrents'
        try:
            subprocess.Popen(['xdg-open', magnet_link],
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
        except:
            if not os.path.exists(directory):
                os.makedirs(directory)
            os.system('wget -O %s/%s.gz %s' %(directory,file_name,torr_file[torrent-1]))
            os.system('gunzip %s/%s.gz' %(directory,file_name))
            download(file_name)
            print '\n\nDownload Complete\n'

    elif platform == "win32":
        directory = 'C:\Users' + user + '\Torrents'
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
            pwrshell = subprocess.Popen([r'C:\WINDOWS\system32\WindowsPowerShell\v1.0\powershell.exe',
                                         '-ExecutionPolicy',
                                         'Unrestricted',
                                         'wget %s -Outfile %s/%s.torrent' %(directory,torr_file, file_name)], cwd=os.getcwd())
            result = pwrshell.wait()
        print '\n'
        download(file_name+'.torrent')
        print '\n\nDownload Complete'n


def fetch():

    link = 'https://kat.cr/full/'

    source_code = requests.get(link)

    plain_text = source_code.text.encode('utf-8')

    soup = BeautifulSoup(plain_text, "lxml")

    global torrent_href
    torrent_name = []
    torrent_seeds = []
    torrent_href = []
    torrent_size = []
    torrent_leechers = []
    movie = []
    tv = []
    music = []
    games = []
    applications = []
    anime = []
    books = []
    losslessmusic = []
    sno = []

    for i in soup.findAll('table', {'class': 'data frontPageWidget'}):
        for j in i('a', {'class': 'cellMainLink'}):
            torrent_name.append(
                ''.join([k if ord(k) < 128 else '' for k in j.get_text()]))
            torrent_href.append(j.get('href'))

        for j in i('td', {'class': 'nobr center'}):
            torrent_size.append(j.get_text())

        for j in i('td', {'class': 'green center'}):
            torrent_seeds.append(j.get_text())

        for j in i('td', {'class': 'red lasttd center'}):
            torrent_leechers.append(j.get_text())

    for i in xrange_(8):
        for j in xrange_(15):
            sno.append(j+1)

    combine = zip(sno,torrent_name, torrent_size, torrent_seeds, torrent_leechers)

    return combine


def movies_torrent():
    torrents = fetch()
    movies = []
    headers = ['SNO.', 'NAME', 'SIZE', 'SEEDS', 'LEECHERS']
    for i in xrange_(15):
        movies.append(torrents[i])

    print '\nLATEST MOVIE TORRENTS\n'
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
                            for i in xrange_(start,end+1):
                                download_torrent('https://kat.cr' + torrent_href[i - 1],movies[i - 1][1])
                elif numbs[0] != '' and numbs[1] == '' :
                    start = int(numbs[0])
                    if start > 0 and start < 16:
                        for i in xrange_(start,16):
                            download_torrent('https://kat.cr' + torrent_href[i - 1],movies[i - 1][1])
                else:
                    end = int(numbs[1])
                    if end > 0 and end < 16:
                        for i in xrange_(1,end+1):
                            download_torrent('https://kat.cr' + torrent_href[i - 1],movies[i - 1][1])
            else:
                for sn in numbs:
                    i = int(sn)
                    if i > 0 and i < 16:
                        download_torrent('https://kat.cr' + torrent_href[i - 1],movies[i - 1][1])
                    else:
                        print "\n\n\tINCORRECT SERIAL NUMBERS....TRY AGAIN!!\n\n"

        else:
            if int(serial) <= 15 and int(serial) >= 1: 
                download_torrent('https://kat.cr' + torrent_href[int(serial) - 1],movies[int(serial) - 1][1])
            else:
                print "\n\n\tINCORRECT SERIAL, TORRRENT DOES NOT EXIST...TRY AGAIN!!\n\n"


def tv_torrent():
    torrents = fetch()
    tv = []
    headers = ['SNO.', 'NAME', 'SIZE', 'SEEDS', 'LEECHERS']
    for i in xrange_(15,30):
        tv.append(torrents[i])

    print '\nLATEST TV TORRENTS\n'
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
                            for i in xrange_(start,end+1):
                                download_torrent('https://kat.cr' + torrent_href[(i+15) - 1],tv[i - 1][1])
                elif numbs[0] != '' and numbs[1] == '' :
                    start = int(numbs[0])
                    if start > 0 and start < 16:
                        for i in xrange_(start,16):
                            download_torrent('https://kat.cr' + torrent_href[(i+15) - 1],tv[i - 1][1])
                else:
                    end = int(numbs[1])
                    if end > 0 and end < 16:
                        for i in xrange_(1,end+1):
                            download_torrent('https://kat.cr' + torrent_href[(i+15) - 1],tv[i - 1][1])
            else:
                for sn in numbs:
                    i = int(sn)
                    if i > 0 and i < 16:
                        download_torrent('https://kat.cr' + torrent_href[(i+15) - 1],tv[i - 1][1])
                    else:
                        print "\n\n\tINCORRECT SERIAL NUMBERS....TRY AGAIN!!\n\n"

        else:
            if int(serial) <= 15 and int(serial) >= 1: 
                download_torrent('https://kat.cr' + torrent_href[(int(serial) + 15) - 1],tv[int(serial) - 1][1])
            else:
                print "\n\n\tINCORRECT SERIAL, TORRRENT DOES NOT EXIST...TRY AGAIN!!\n\n"


def music_torrent():
    torrents = fetch()
    music = []
    headers = ['SNO.', 'NAME', 'SIZE', 'SEEDS', 'LEECHERS']
    for i in xrange_(30,45):
        music.append(torrents[i])

    print '\nLATEST MUSIC TORRENTS\n'
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
                            for i in xrange_(start,end+1):
                                download_torrent('https://kat.cr' + torrent_href[(i+30) - 1],music[i - 1][1])
                elif numbs[0] != '' and numbs[1] == '' :
                    start = int(numbs[0])
                    if start > 0 and start < 16:
                        for i in xrange_(start,16):
                            download_torrent('https://kat.cr' + torrent_href[(i+30) - 1],music[i - 1][1])
                else:
                    end = int(numbs[1])
                    if end > 0 and end < 16:
                        for i in xrange_(1,end+1):
                            download_torrent('https://kat.cr' + torrent_href[(i+30) - 1],music[i - 1][1])
            else:
                for sn in numbs:
                    i = int(sn)
                    if i > 0 and i < 16:
                        download_torrent('https://kat.cr' + torrent_href[(i+30) - 1],music[i - 1][1])
                    else:
                        print "\n\n\tINCORRECT SERIAL NUMBERS....TRY AGAIN!!\n\n"

        else:
            if int(serial) <= 15 and int(serial) >= 1: 
                download_torrent('https://kat.cr' + torrent_href[(int(serial) + 30) - 1],music[int(serial) - 1][1])
            else:
                print "\n\n\tINCORRECT SERIAL, TORRRENT DOES NOT EXIST...TRY AGAIN!!\n\n"


def games_torrent():
    torrents = fetch()
    games = []
    headers = ['SNO.', 'NAME', 'SIZE', 'SEEDS', 'LEECHERS']
    for i in xrange_(45,60):
        games.append(torrents[i])

    print '\nLATEST GAME TORRENTS\n'
    print(tabulate(games, headers, tablefmt='psql', numalign="center"))
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
                            for i in xrange_(start,end+1):
                                download_torrent('https://kat.cr' + torrent_href[(i+45) - 1],games[i - 1][1])
                elif numbs[0] != '' and numbs[1] == '' :
                    start = int(numbs[0])
                    if start > 0 and start < 16:
                        for i in xrange_(start,16):
                            download_torrent('https://kat.cr' + torrent_href[(i+45) - 1],games[i - 1][1])
                else:
                    end = int(numbs[1])
                    if end > 0 and end < 16:
                        for i in xrange_(1,end+1):
                            download_torrent('https://kat.cr' + torrent_href[(i+45) - 1],games[i - 1][1])
            else:
                for sn in numbs:
                    i = int(sn)
                    if i > 0 and i < 16:
                        download_torrent('https://kat.cr' + torrent_href[(i+45) - 1],games[i - 1][1])
                    else:
                        print "\n\n\tINCORRECT SERIAL NUMBERS....TRY AGAIN!!\n\n"

        else:
            if int(serial) <= 15 and int(serial) >= 1: 
                download_torrent('https://kat.cr' + torrent_href[(int(serial) + 45) - 1],games[int(serial) - 1][1])
            else:
                print "\n\n\tINCORRECT SERIAL, TORRRENT DOES NOT EXIST...TRY AGAIN!!\n\n"


def applications_torrent():
    torrents = fetch()
    applications = []
    headers = ['SNO.', 'NAME', 'SIZE', 'SEEDS', 'LEECHERS']
    for i in xrange_(60,75):
        applications.append(torrents[i])

    print '\nLATEST APPLICATION TORRENTS\n'
    print(tabulate(applications, headers, tablefmt='psql', numalign="center"))
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
                            for i in xrange_(start,end+1):
                                download_torrent('https://kat.cr' + torrent_href[(i+60) - 1],applications[i - 1][1])
                elif numbs[0] != '' and numbs[1] == '' :
                    start = int(numbs[0])
                    if start > 0 and start < 16:
                        for i in xrange_(start,16):
                            download_torrent('https://kat.cr' + torrent_href[(i+60) - 1],applications[i - 1][1])
                else:
                    end = int(numbs[1])
                    if end > 0 and end < 16:
                        for i in xrange_(1,end+1):
                            download_torrent('https://kat.cr' + torrent_href[(i+60) - 1],applications[i - 1][1])
            else:
                for sn in numbs:
                    i = int(sn)
                    if i > 0 and i < 16:
                        download_torrent('https://kat.cr' + torrent_href[(i+60) - 1],applications[i - 1][1])
                    else:
                        print "\n\n\tINCORRECT SERIAL NUMBERS....TRY AGAIN!!\n\n"

        else:
            if int(serial) <= 15 and int(serial) >= 1: 
                download_torrent('https://kat.cr' + torrent_href[(int(serial) + 60) - 1],applications[int(serial) - 1][1])
            else:
                print "\n\n\tINCORRECT SERIAL, TORRRENT DOES NOT EXIST...TRY AGAIN!!\n\n"



def anime_torrent():
    torrents = fetch()
    anime = []
    headers = ['SNO.', 'NAME', 'SIZE', 'SEEDS', 'LEECHERS']
    for i in xrange_(75,90):
        anime.append(torrents[i])

    print '\nLATEST ANIME TORRENTS\n'
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
                            for i in xrange_(start,end+1):
                                download_torrent('https://kat.cr' + torrent_href[(i+75) - 1],anime[i - 1][1])
                elif numbs[0] != '' and numbs[1] == '' :
                    start = int(numbs[0])
                    if start > 0 and start < 16:
                        for i in xrange_(start,16):
                            download_torrent('https://kat.cr' + torrent_href[(i+75) - 1],anime[i - 1][1])
                else:
                    end = int(numbs[1])
                    if end > 0 and end < 16:
                        for i in xrange_(1,end+1):
                            download_torrent('https://kat.cr' + torrent_href[(i+75) - 1],anime[i - 1][1])
            else:
                for sn in numbs:
                    i = int(sn)
                    if i > 0 and i < 16:
                        download_torrent('https://kat.cr' + torrent_href[(i+75) - 1],anime[i - 1][1])
                    else:
                        print "\n\n\tINCORRECT SERIAL NUMBERS....TRY AGAIN!!\n\n"

        else:
            if int(serial) <= 15 and int(serial) >= 1: 
                download_torrent('https://kat.cr' + torrent_href[(int(serial) + 75) - 1],anime[int(serial) - 1][1])
            else:
                print "\n\n\tINCORRECT SERIAL, TORRRENT DOES NOT EXIST...TRY AGAIN!!\n\n"


def books_torrent():
    torrents = fetch()
    books = []
    headers = ['SNO.', 'NAME', 'SIZE', 'SEEDS', 'LEECHERS']
    for i in xrange_(90,105):
        books.append(torrents[i])

    print '\nLATEST BOOK TORRENTS\n'
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
                            for i in xrange_(start,end+1):
                                download_torrent('https://kat.cr' + torrent_href[(i+90) - 1],books[i - 1][1])
                elif numbs[0] != '' and numbs[1] == '' :
                    start = int(numbs[0])
                    if start > 0 and start < 16:
                        for i in xrange_(start,16):
                            download_torrent('https://kat.cr' + torrent_href[(i+90) - 1],books[i - 1][1])
                else:
                    end = int(numbs[1])
                    if end > 0 and end < 16:
                        for i in xrange_(1,end+1):
                            download_torrent('https://kat.cr' + torrent_href[(i+90) - 1],books[i - 1][1])
            else:
                for sn in numbs:
                    i = int(sn)
                    if i > 0 and i < 16:
                        download_torrent('https://kat.cr' + torrent_href[(i+90) - 1],books[i - 1][1])
                    else:
                        print "\n\n\tINCORRECT SERIAL NUMBERS....TRY AGAIN!!\n\n"

        else:
            if int(serial) <= 15 and int(serial) >= 1: 
                download_torrent('https://kat.cr' + torrent_href[(int(serial) + 90) - 1],books[int(serial) - 1][1])
            else:
                print "\n\n\tINCORRECT SERIAL, TORRRENT DOES NOT EXIST...TRY AGAIN!!\n\n"

def losslessmusic_torrent():
    torrents = fetch()
    losslessmusic = []
    headers = ['SNO.', 'NAME', 'SIZE', 'SEEDS', 'LEECHERS']
    for i in xrange_(105,120):
        losslessmusic.append(torrents[i])

    print '\nLATEST LOSSLESS MUSIC TORRENTS\n'
    print(tabulate(losslessmusic, headers, tablefmt='psql', numalign="center"))
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
                            for i in xrange_(start,end+1):
                                download_torrent('https://kat.cr' + torrent_href[(i+105) - 1],losslessmusic[i - 1][1])
                elif numbs[0] != '' and numbs[1] == '' :
                    start = int(numbs[0])
                    if start > 0 and start < 16:
                        for i in xrange_(start,16):
                            download_torrent('https://kat.cr' + torrent_href[(i+105) - 1],losslessmusic[i - 1][1])
                else:
                    end = int(numbs[1])
                    if end > 0 and end < 16:
                        for i in xrange_(1,end+1):
                            download_torrent('https://kat.cr' + torrent_href[(i+105) - 1],losslessmusic[i - 1][1])
            else:
                for sn in numbs:
                    i = int(sn)
                    if i > 0 and i < 16:
                        download_torrent('https://kat.cr' + torrent_href[(i+105) - 1],losslessmusic[i - 1][1])
                    else:
                        print "\n\n\tINCORRECT SERIAL NUMBERS....TRY AGAIN!!\n\n"

        else:
            if int(serial) <= 15 and int(serial) >= 1: 
                download_torrent('https://kat.cr' + torrent_href[(int(serial) + 105) - 1],losslessmusic[int(serial) - 1][1])
            else:
                print "\n\n\tINCORRECT SERIAL, TORRRENT DOES NOT EXIST...TRY AGAIN!!\n\n"