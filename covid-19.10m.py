#!/usr/bin/env PYTHONIOENCODING=UTF-8 /usr/local/bin/python3
# pylint3: disable=C0103,W0123

import urllib.request
import urllib.parse
import urllib.error
import json

def getValue(result, countryCode):
    return list(filter(lambda x : x['country_code']==countryCode,result['confirmed']['locations']))

url = 'https://coronavirus-tracker-api.herokuapp.com/all'
response = urllib.request.urlopen(url)
result = json.loads(response.read())
str='\u271D {%f}| color=red () | color=green'.format(result['latest']['confirmed'])
print(str)
print("---")

strIT='IT \u271D {%f}| color=red () | color=green'.format(getValue(result, 'IT')['latest']) 
print(strIT)
print("---")

strNL='NL \u271D {}| color=red () | color=green'.format(getValue(result, 'NL')['latest']) 
print(strNL)
print("---")

