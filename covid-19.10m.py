#!/usr/bin/env PYTHONIOENCODING=UTF-8 /usr/local/bin/python3
# pylint3: disable=C0103,W0123

import urllib.request
import urllib.parse
import urllib.error
import json
import locale
import requests

# Use '' for auto, or force e.g. to 'en_US.UTF-8'
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')


def getValue(result, countryCode):
    return list(filter(lambda x: x['country'].lower() == countryCode.lower(), result))[0]


url = "https://corona.lmao.ninja/all"
response = requests.request("GET", url, headers={}, data={})
result = json.loads(response.text)
strWrld = '\u271D {:n}| color=red'.format(
    result['cases']
)
print(strWrld)
print("---")

urlCountries = 'https://corona.lmao.ninja/countries'
responseCountries = requests.request("GET", urlCountries, headers={}, data={})
resultCountries = json.loads(responseCountries.text)

countries = [
    {'code': 'IT', 'name': 'Italy'},
    {'code': 'NL', 'name': 'Netherlands'},
    {'code': 'CH', 'name': 'China'},
]

for country in countries:
    try:
        str = '{} \u271D {:n}| color=red'.format(
            country['code'],
            getValue(resultCountries, country['name'])['cases']
        )
        print(str)
        print("---")
    except:
        print('{} N/A'.format(country['code']))
        print("---")


# strIT = 'IT \u271D {:n}| color=red'.format(
#     getValue(resultCountries, 'Italy')['cases']
# )
# print(strIT)
# print("---")

# strNL = 'NL \u271D {:n}| color=red'.format(
#     getValue(resultCountries, 'Netherlands')['cases']
# )
# print(strNL)
# print("---")

# strCH = 'CH \u271D {:n}| color=red'.format(
#     getValue(resultCountries, 'China')['cases']
# )
# print(strCH)
# print("---")
