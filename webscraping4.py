#! python2.7
import requests, bs4
from bs4 import BeautifulSoup

res = requests.get('http://www.residentadvisor.net/clubs.aspx')
res.raise_for_status()

#### scraping page
clubSoup = bs4.BeautifulSoup(res.text,'html.parser')
elems = clubSoup.find(class_='fl col4-6')
playFile = open('Clubs.txt', 'wb')

for row in elems.find_all(class_='clearfix'):
	if row.find(class_='fl grey mobile-off').contents:
		name = row.find('a').contents[0]
		address = row.find(class_='fl grey mobile-off').contents[0]

		### finding the geo_loc
		geo_loc = requests.get('http://www.mapquestapi.com/geocoding/v1/address?key=MSJ6rAyYJeKQdpYsUqkqbaAAGH6y5VFK&location=%s&callback=renderGeocode' % (address), timeout=0.03)
		geo_loc.raise_for_status

		playFile.write(name + " ! " + address + " ! " + geo_loc + '\n')

playFile.close()
