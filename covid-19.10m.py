#!/usr/bin/env PYTHONIOENCODING=UTF-8 /usr/local/bin/python3
# pylint3: disable=C0103,W0123

import urllib.request
import urllib.parse
import urllib.error
import json
import locale
import requests

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')  # Use '' for auto, or force e.g. to 'en_US.UTF-8'


def getValue(result, countryCode):
    return list(filter(lambda x: x['country'] == countryCode, result))[0]


url = "https://corona.lmao.ninja/all"
response = requests.request("GET", url, headers={}, data = {})
result = json.loads(response.text)
strWrld = '\u271D {:n}| color=red'.format(
    result['cases']
)
print(strWrld)
print("---")

urlCountries = 'https://corona.lmao.ninja/countries'
responseCountries = requests.request("GET", urlCountries, headers={}, data = {})
resultCountries = json.loads(responseCountries.text)

strIT = 'IT \u271D {:n}| color=red'.format(
    getValue(resultCountries, 'Italy')['cases']
)
print(strIT)
print("---")

strNL = 'NL \u271D {:n}| color=red'.format(
    getValue(resultCountries, 'Netherlands')['cases']
)
print(strNL)
print("---")
