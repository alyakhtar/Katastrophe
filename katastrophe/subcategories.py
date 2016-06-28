import requests
import sys
from bs4 import BeautifulSoup
from tabulate import tabulate
import subprocess
from sys import platform
import os
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


def print_table(serial, torrent, size, seeds, leechers):
    table = zip(serial, torrent, size, seeds, leechers)
    if not table:
        print('\n\tNOTHING FOUND !')
        exit()
    else:
        headers = ['S.No.', 'Torrent Name', 'Size', 'Seeders', 'Leechers']
        print(tabulate(table, headers, tablefmt='psql', numalign="center"))


def url_generator(url, page, category):
	category_list = ['movies', 'tv', 'anime', 'music',
	    'books', 'games', 'applications', 'xxx']
	words = url.split()

	if len(words) == 1:
		link = 'https://kat.cr/usearch/' + words[0] + '%' + '20category%3' + 'A' + category_list[category]
	else:
		for i in xrange_(len(words)):
			if i == 0:
				link = 'https://kat.cr/usearch/' + words[i]
			else:
				link += '%20' + words[i]
		link += '%' + '20category%3' + 'A' + category_list[category]
                
	if page == 1:
		return link + '/' 
	return link + '/' + str(page) + '/'


def download_torrent(torrent):	
	file_name = "".join(torr[torrent-1].split())
	user = getpass.getuser()    

	if platform == "linux" or platform == "linux2" or platform == "darwin":
		directory = '/home/'+ user +'/Torrents'
		try:
		    subprocess.Popen(['xdg-open', mag[torrent - 1]],
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
		    subprocess.Popen([exe.decode(), mag[torrent - 1]])
		else:
		    if not os.path.exists(directory):
		        os.makedirs(directory)
		    # print("\nPlease Install/Run BitTorrent, uTorrent, or deluge.\n")
		    pwrshell = subprocess.Popen([r'C:\WINDOWS\system32\WindowsPowerShell\v1.0\powershell.exe',
		                     '-ExecutionPolicy',
		                     'Unrestricted',
		                     'wget %s -Outfile %s/%s.torrent' %(directory,torr_file[torrent-1],file_name)], cwd=os.getcwd())
		    result = pwrshell.wait()
		    print '\n'
		    download(file_name+'.torrent')
		    print '\n\nDownload Complete\n'



def by_movies(url,page):
	link = url_generator(url, page, 0)
	source_code = requests.get(link)
	plain_text = source_code.text.encode('utf-8')
	soup = BeautifulSoup(plain_text, "lxml")

	global mag
	global torr_file
	global torr
	torr = []
	torr_file = []
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

def by_tv(url,page):
	link = url_generator(url, page, 1)
	source_code = requests.get(link)
	plain_text = source_code.text.encode('utf-8')
	soup = BeautifulSoup(plain_text, "lxml")

	global mag
	global torr_file
	global torr
	torr = []
	torr_file = []
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

def by_anime(url,page):
	link = url_generator(url, page, 2)
	source_code = requests.get(link)
	plain_text = source_code.text.encode('utf-8')
	soup = BeautifulSoup(plain_text, "lxml")

	global mag
	global torr_file
	global torr
	torr = []
	torr_file = []
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

def by_music(url,page):
	link = url_generator(url, page, 3)
	source_code = requests.get(link)
	plain_text = source_code.text.encode('utf-8')
	soup = BeautifulSoup(plain_text, "lxml")

	global mag
	global torr_file
	global torr
	torr = []
	torr_file = []
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

def by_books(url,page):
	link = url_generator(url, page, 4)
	source_code = requests.get(link)
	plain_text = source_code.text.encode('utf-8')
	soup = BeautifulSoup(plain_text, "lxml")

	global mag
	global torr_file
	global torr
	torr = []
	torr_file = []
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

def by_games(url,page):
	link = url_generator(url, page, 5)
	source_code = requests.get(link)
	plain_text = source_code.text.encode('utf-8')
	soup = BeautifulSoup(plain_text, "lxml")

	global mag
	global torr_file
	global torr
	torr = []
	torr_file = []
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

def by_applications(url,page):
	link = url_generator(url, page, 6)
	source_code = requests.get(link)
	plain_text = source_code.text.encode('utf-8')
	soup = BeautifulSoup(plain_text, "lxml")

	global mag
	global torr_file
	global torr
	torr = []
	torr_file = []
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

def by_xxx(url,page):
	link = url_generator(url, page, 7)
	source_code = requests.get(link)
	plain_text = source_code.text.encode('utf-8')
	soup = BeautifulSoup(plain_text, "lxml")

	global mag
	global torr_file
	global torr
	torr = []
	torr_file = []
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

def xxx_torrent():
    link = 'https://kat.cr/xxx/1/?field=time_add&sorder=desc'
    source_code = requests.get(link)
    plain_text = source_code.text.encode('utf-8')
    soup = BeautifulSoup(plain_text, "lxml")

    global mag
    global torr_file
    global torr
    torr = []
    torr_file = []
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

    table = zip(sno, torr, sz, sd, lc)
    if not table:
        print('\n\tNOTHING FOUND !')
        exit()
    else:
        headers = ['S.No.', 'Torrent Name', 'Size', 'Seeders', 'Leechers']
        print(tabulate(table, headers, tablefmt='psql', numalign="center"))

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
                        if end < 26 and start > 0:
                            for i in xrange(start,end+1):
                                download_torrent(i)
                elif numbs[0] != '' and numbs[1] == '' :
                    start = int(numbs[0])
                    if start > 0 and start < 26:
                        for i in xrange(start,26):
                            download_torrent(i)
                else:
                    end = int(numbs[1])
                    if end > 0 and end < 26:
                        for i in xrange(1,end+1):
                            download_torrent(i)
            else:
                for sn in numbs:
                    i = int(sn)
                    if i > 0 and i < 26:
                        download_torrent(i)
                    else:
                        print "\n\n\tINCORRECT SERIAL NUMBERS!!\n\n"

        else:
            if int(serial) <= 25 and int(serial) >= 1: 
                download_torrent(i)
            else:
                print "\n\n\tINCORRECT SERIAL, TORRRENT DOES NOT EXIST!!\n\n"


def categories(category):
    page = 1
    category_list = ['movies', 'tv', 'anime', 'music',
	    'books', 'games', 'applications', 'xxx']
    print("Torrent Search : "),
    query = raw_input_()
    table = getattr(sys.modules[__name__], 'by_%s' % category_list[category])(query, page)

    while True:
        print('Enter torrent No.(s) to download or m for more or b for back or e to exit : '),
        serial = raw_input_()
        if serial == 'm' or serial == 'M':
            page += 1
            getattr(sys.modules[__name__], 'by_%s' % category_list[category])(query, page)
        elif serial == 'b' or serial == 'B':
            if page != 1:
                page -= 1
                getattr(sys.modules[__name__], 'by_%s' % category_list[category])(query, page)
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
                            print "\n\n\tINCORRECT SERIAL NUMBERS!!\n\n"
                    break

            else:
                if int(serial) <= 25 and int(serial) >= 1: 
                    download_torrent(int(serial))
                    break
                else:
                    print "\n\n\tINCORRECT SERIAL, TORRRENT DOES NOT EXIST!!\n\n"
