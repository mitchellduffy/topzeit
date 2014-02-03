import requests
from requests.auth import HTTPBasicAuth
import config
import json

import logging

# These two lines enable debugging at httplib level (requests->urllib3->httplib)
# You will see the REQUEST, including HEADERS and DATA, and RESPONSE with HEADERS but without DATA.
# The only thing missing will be the response.body which is not logged.
import httplib
httplib.HTTPConnection.debuglevel = 1

# You must initialize logging, otherwise you'll not see debug output.
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True






# get the API credentials from config.py
cfg = config.get_die_zeit_credentials()

# set parameters for the query
payload = {'q': '*:*', 'fields': '*', 'limit': '1', 'offset': '0'}



r = requests.get(
        url = cfg['endpoint'],
        params = payload,
        auth = HTTPBasicAuth('X-Authorization', cfg['api_key'])
        )


if r.status_code != requests.codes.ok:
    r.raise_for_status()
else:
    print r.json()




#for











