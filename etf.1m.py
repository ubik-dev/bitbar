#!/usr/bin/env PYTHONIOENCODING=UTF-8 /usr/local/bin/python3
# pylint3: disable=C0103,W0123

import urllib.request
import urllib.parse
import urllib.error
import json


url = 'https://query1.finance.yahoo.com/v8/finance/chart/VWRL.AS?region=US&lang=en-US&includePrePost=false&interval=2m&range=1d&corsDomain=finance.yahoo.com&.tsrc=finance'

response = urllib.request.urlopen(url)
result = json.loads(response.read())
str='VWRL (€{})| color=white'.format(result['chart']['result'][0]['meta']['regularMarketPrice'])
print(str)