#! /usr/bin/python3
import json
import requests, bs4
import urllib.parse, urllib.request
import secrets

res = requests.get('http://www.residentadvisor.net/clubs.aspx')
res.raise_for_status()

#### scraping page for clubs names
clubSoup = bs4.BeautifulSoup(res.text,'html.parser')
elems = clubSoup.find(class_='fl col4-6')

all_addresses = []

for row in elems.find_all(class_='clearfix'):
        if row.find(class_='fl grey mobile-off').contents:
                name = row.find('a').contents[0]
                address = row.find(class_='fl grey mobile-off').contents[0]
                all_addresses.append((name, address))

### calling mapquest to obtain geoloc
playFile = open('Clubs.txt', 'w')
for address in all_addresses:
        enc_address = urllib.parse.quote(address[1], "utf-8")
        with urllib.request.urlopen('http://www.mapquestapi.com/geocoding/v1/address?key=%s&location=%s' % (secrets.mapquest_key, enc_address)) as geo_loc:
                obj = json.loads(geo_loc.read().decode("utf-8"))
                ll = obj["results"][0]["locations"][0]["displayLatLng"]
                playFile.write(address[0] + " ! " + address[1] + " ! " + str(ll["lat"]) + " ! " + str(ll["lng"]) + '\n')

