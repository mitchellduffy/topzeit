import requests
from requests.auth import HTTPBasicAuth
import json

#import logging
#
## These two lines enable debugging at httplib level (requests->urllib3->httplib)
## You will see the REQUEST, including HEADERS and DATA, and RESPONSE with HEADERS but without DATA.
## The only thing missing will be the response.body which is not logged.
#import httplib
#httplib.HTTPConnection.debuglevel = 1
#
## You must initialize logging, otherwise you'll not see debug output.
#logging.basicConfig()
#logging.getLogger().setLevel(logging.DEBUG)
#requests_log = logging.getLogger("requests.packages.urllib3")
#requests_log.setLevel(logging.DEBUG)
#requests_log.propagate = True



# set parameters for the query

endpoint = 'http://api.zeit.de/content?'

payload = {
        'q': '*:*',
        'fields': '*',
        'limit': '1',
        'offset': '0'
}

auth = {'X-Authorization': '4dc7a859b685d0e9b0ec20fd4382e349e6c734f5c02b7b5ba400'}



r = requests.get(
        url = endpoint,
        params = payload,
        headers = auth
        )


if r.status_code != requests.codes.ok:
    r.raise_for_status()
else:
    print r.json()




#for











