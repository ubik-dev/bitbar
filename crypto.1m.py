#!/usr/bin/env PYTHONIOENCODING=UTF-8 /usr/local/bin/python3
# pylint: disable=C0103,W0123

import urllib.request
import urllib.parse
import urllib.error
import json
import locale
import os
import yaml


locale.setlocale(locale.LC_ALL, 'en_US')

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
        "code": "xbt",
        "url":  "https://api.kraken.com/0/public/Ticker?pair=XXBTZEUR",
        # "url": "https://coinmarketcap-nexuist.rhcloud.com/api/eth",
        "getRate": lambda value: float(value['result']['XXBTZEUR']['c'][0]),
        "quantity": eval('{}'.format(cfg['xbt']['quantity'])),
        "eurQty": eval('{}'.format(cfg['xbt']['eurQty']))
    },
    {
        "code": "xrp",
        "url":  "https://api.kraken.com/0/public/Ticker?pair=XXRPZEUR",
        # "url": "https://coinmarketcap-nexuist.rhcloud.com/api/xrp",
        "getRate": lambda value: float(value['result']['XXRPZEUR']['c'][0]),
        "quantity": eval('{}'.format(cfg['xrp']['quantity'])),
        "eurQty": eval('{}'.format(cfg['xrp']['eurQty']))
    },
    {
        "code": "xem",
        "url": "https://api.coinmarketcap.com/v1/ticker/nem/?convert=EUR",
        "getRate": lambda value: float(value[0]['price_eur']),
        "quantity": eval('{}'.format(cfg['xem']['quantity'])),
        "eurQty": eval('{}'.format(cfg['xem']['eurQty']))
    },
    {
        "code": "xlm",
        "url":  "https://api.coinmarketcap.com/v1/ticker/stellar/?convert=EUR",
        # "url": "https://coinmarketcap-nexuist.rhcloud.com/api/xlm",
        "getRate": lambda value: float(value[0]['price_eur']),
        "quantity": eval('{}'.format(cfg['xlm']['quantity'])),
        "eurQty": eval('{}'.format(cfg['xlm']['eurQty']))
    },
    {
        "code": "bcn",
        "url": "https://api.coinmarketcap.com/v1/ticker/bytecoin-bcn/?convert=EUR",
        "getRate": lambda value: float(value[0]['price_eur']),
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
    currency = key
    response = urllib.request.urlopen(currency["url"])
    result = json.loads(response.read())
    boughtRate = currency["eurQty"] / currency["quantity"]
    currentRate = currency["currRate"] = currency['getRate'](result)
    currentAmount = (currency["currRate"] * currency["quantity"])
    boughtAmount = currency["eurQty"]
    currency["currProfit"] = diff = currentAmount - boughtAmount
    currentProfitPerc = currency["currProfitPerc"] = diff / boughtAmount * 100
    totals["total"] += diff
    if currency["code"] != "eth":
        totals["noEtherTotalDiff"] += diff
        totals["noEtherQtyEuro"] += boughtAmount

    currency["print"] = "€{:<18}{:<15}{}%| color={}".format(
        locale.format("%.2f", diff, grouping=True),
        locale.format("%.4f", currentRate, grouping=True),
        locale.format("%.2f", currentProfitPerc, grouping=True),
        'green' if diff > 0 else 'red'
    )

totals["print"] = 'Total\n€{:<18}({}%)'.format(
    locale.format("%.2f", totals["total"], grouping=True),
    locale.format("%.2f", totals["noEtherTotalDiff"] /
                  totals["noEtherQtyEuro"] * 100, grouping=True)
)

# printing
print("{}% ({})%|color={}".format(
    locale.format("%.2f", currencies[0]
                  ["currProfitPerc"], grouping=True),
    locale.format("%.2f", totals["noEtherTotalDiff"] /
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
