#!/usr/bin/env PYTHONIOENCODING=UTF-8 /usr/local/bin/python3
# pylint3: disable=C0103,W0123

import urllib.request
import urllib.parse
import urllib.error
import json
import locale
import os
import yaml


locale.setlocale(locale.LC_ALL, 'en_US')
yaml.warnings({'YAMLLoadWarning': False})
with open(os.path.dirname(os.path.abspath(__file__)) + "/.env.yaml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)


currencies = [
    {
        "code": "eth",
        "url":  "https://api.kraken.com/0/public/Ticker?pair=XETHZEUR",
        # "url": "https://coinmarketcap-nexuist.rhcloud.com/api/eth",
        "getRate": lambda value: float(value['result']['XETHZEUR']['c'][0]),
        "quantity": eval('{}'.format(cfg['eth']['quantity'])),
        "eurQty": eval('{}'.format(cfg['eth']['eurQty']))
    },
    
    {
        "code": "eur",
        "url":  "https://api.kraken.com/0/public/Ticker?pair=EOSEUR",
        "getRate": lambda value: float(1.0),
        "quantity": eval('{}'.format(cfg['eur']['quantity'])),
        "eurQty": eval('{}'.format(cfg['eur']['eurQty']))
    },
    {
        "code": "xbt",
        "url":  "https://api.kraken.com/0/public/Ticker?pair=XXBTZEUR",
        "getRate": lambda value: float(value['result']['XXBTZEUR']['c'][0]),
        "quantity": eval('{}'.format(cfg['xbt']['quantity'])),
        "eurQty": eval('{}'.format(cfg['xbt']['eurQty']))
    },
    {
        "code": "xrp",
        "url":  "https://api.kraken.com/0/public/Ticker?pair=XXRPZEUR",
        "getRate": lambda value: float(value['result']['XXRPZEUR']['c'][0]),
        "quantity": eval('{}'.format(cfg['xrp']['quantity'])),
        "eurQty": eval('{}'.format(cfg['xrp']['eurQty']))
    },
    {
        "code": "xem",
        "url": "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?convert=EUR&symbol=XEM",
        "getRate": lambda value: float(value['data']['XEM']['quote']['EUR']['price']),
        "quantity": eval('{}'.format(cfg['xem']['quantity'])),
        "eurQty": eval('{}'.format(cfg['xem']['eurQty']))
    },
    {
        "code": "xlm",
        # "url":  "https://api.coinmarketcap.com/v1/ticker/stellar/?convert=EUR",
        "url": "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?convert=EUR&symbol=XLM",
        "getRate": lambda value: float(value['data']['XLM']['quote']['EUR']['price']),
        "quantity": eval('{}'.format(cfg['xlm']['quantity'])),
        "eurQty": eval('{}'.format(cfg['xlm']['eurQty']))
    },
    {
        "code": "bcn",
        "url": "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?convert=EUR&symbol=BCN",
        "getRate": lambda value: float(value['data']['BCN']['quote']['EUR']['price']),
        "quantity": eval('{}'.format(cfg['bcn']['quantity'])),
        "eurQty": eval('{}'.format(cfg['bcn']['eurQty']))
    }
]
totals = {
    "total": 0.0,
    "noEtherTotalDiff": 0.0,
    "noEtherQtyEuro": 0.0,
    "print": ""
}

# calculations
for key in sorted(currencies, key=lambda x: x["eurQty"], reverse=True):
    try:
        currency = key
        req = urllib.request.Request(
            currency["url"],
            None,
            {
                'Accepts': 'application/json',
                'X-CMC_PRO_API_KEY': cfg['coinmarketcapApiKey'],
            }
        )
        response = urllib.request.urlopen(req)
        result = json.loads(response.read())
        boughtRate = currency["eurQty"] / currency["quantity"] if currency["quantity"]>0 else 0
        currentRate = currency["currRate"] = currency['getRate'](result)
        currentAmount = (currency["currRate"] * currency["quantity"])
        boughtAmount = currency["eurQty"]
        currency["currProfit"] = diff = currentAmount - boughtAmount
        currentProfitPerc =  (diff / boughtAmount * 100) if boughtAmount > 0 and diff >0  else 0 
        currency["currProfitPerc"] = currentProfitPerc
        totals["total"] += diff
        
        if currency["code"] != "eth":
            totals["noEtherTotalDiff"] += diff
            totals["noEtherQtyEuro"] += boughtAmount

        currency["print"] = "€{:<18}{:<15}{}%| color={}".format(
            locale.format_string("%.2f", diff, grouping=True),
            locale.format_string("%.4f", currentRate, grouping=True),
            locale.format_string("%.2f", currentProfitPerc, grouping=True),
            'green' if diff > 0 else 'red'
        )
        
    except:
        currency["print"] = "N/A| color=red"
        totals["total"] += 0


totals["print"] = 'Total\n€{:<18}({}%)'.format(
    locale.format_string("%.2f", totals["total"], grouping=True),
    locale.format_string("%.2f", totals["noEtherTotalDiff"] /
                         totals["noEtherQtyEuro"] * 100, grouping=True)
)

# printing
print("{}% (₿{}%)|color={}".format(
    locale.format_string("%.2f", currencies[0]
                         ["currProfitPerc"], grouping=True),
    locale.format_string("%.2f", totals["noEtherTotalDiff"] /
                         totals["noEtherQtyEuro"] * 100, grouping=True),
    'green' if totals["noEtherTotalDiff"] > 0 else 'red'
))
print("---")
for key in sorted(currencies, key=lambda x: x["eurQty"], reverse=True):
    currency = key
    print(currency["code"])
    print(currency["print"])
    print("---")

print(totals["print"])
