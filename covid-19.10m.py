#!/usr/bin/env PYTHONIOENCODING=UTF-8 /usr/local/bin/python3
# pylint3: disable=C0103,W0123

import urllib.request
import urllib.parse
import urllib.error
import json


url = 'https://coronavirus-tracker-api.herokuapp.com/all'
response = urllib.request.urlopen(url)
result = json.loads(response.read())
str='\u271D {}| color=red () | color=green'.format(result['latest']['confirmed'])
print(str)
print("---")
valueIT=list(filter(lambda x : x['country_code']=='IT',result['confirmed']['locations']))[0]
strIT='IT \u271D {}| color=red () | color=green'.format(valueIT['latest']) 
print(strIT)
print("---")
valueNL=list(filter(lambda x : x['country_code']=='NL',result['confirmed']['locations']))[0]
strNL='NL \u271D {}| color=red () | color=green'.format(valueNL['latest']) 
print(strNL)
