#!/usr/bin/env python
import requests
import json

params = {
    'q' : 'subtitle:walfang',
    'limit' : '100',
    'fields' : 'subtitle,uri'
}

url = 'http://api.zeit.de/content?'
headers = {'X-Authorization': '4dc7a859b685d0e9b0ec20fd4382e349e6c734f5c02b7b5ba400'}

r = requests.get(url, params=params, headers=headers)

#print r.json()

json = r.json()

for result in json['matches']:
    print result['subtitle']
    print result['uri']
    print
