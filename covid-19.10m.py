#!/usr/bin/env PYTHONIOENCODING=UTF-8 /usr/local/bin/python3
# pylint3: disable=C0103,W0123

import urllib.request
import urllib.parse
import urllib.error
import json
import locale

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')  # Use '' for auto, or force e.g. to 'en_US.UTF-8'


def getValue(result, countryCode):
    return list(filter(lambda x: x['country_code'] == countryCode, result['confirmed']['locations']))[0]


url = 'https://coronavirus-tracker-api.herokuapp.com/all'
response = urllib.request.urlopen(url)
result = json.loads(response.read())

strWrld = '\u271D {:n}| color=red'.format(
    result['latest']['confirmed']
)
print(strWrld)
print("---")

strIT = 'IT \u271D {:n}| color=red'.format(
    getValue(result, 'IT')['latest']
)
print(strIT)
print("---")

strNL = 'NL \u271D {:n}| color=red'.format(
    getValue(result, 'NL')['latest']
)
print(strNL)
print("---")
