import requests
from bs4 import BeautifulSoup


def download_torrent(link):
	source_code = requests.get(link)

	plain_text = source_code.text.encode('utf-8')

	soup = BeautifulSoup(plain_text, "lxml")

	magnet = soup.find('a',{'title':'Magnet link'})
	magnet_link = magnet.get('href')