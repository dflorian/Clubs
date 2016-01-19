#! python2.7
import requests, bs4
from bs4 import BeautifulSoup

res = requests.get('http://www.residentadvisor.net/clubs.aspx')
res.raise_for_status()

clubSoup = bs4.BeautifulSoup(res.text,'html.parser')
elems = clubSoup.find(class_='fl col4-6')
playFile = open('Clubs.txt', 'wb')
for row in elems.find_all(class_='clearfix'):
	if row.find(class_='fl grey mobile-off').contents:
		playFile.write(row.find('a').contents[0] + "/" + row.find(class_='fl grey mobile-off').contents[0] + '\n')

playFile.close()