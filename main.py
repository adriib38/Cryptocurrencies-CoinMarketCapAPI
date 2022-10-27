import requests
import time

headers = {
        'X-CMC_PRO_API_KEY': 'YOUR_API_KEY',
        'Accepts': 'application/json'
        }

params = {
        'start': '1',
        'limit': '6',
        'convert': 'EUR'
        }

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

json = requests.get(url, params = params, headers = headers).json()

coins = json['data']

for coin in coins:
    if coin['symbol'] == 'BTC':
      print(coin['symbol'])
      print(round(coin['quote']['EUR']['price'],5))
    if coin['symbol'] == 'ETH':
      print(coin['symbol'])
      print(round(coin['quote']['EUR']['price'],5))
        


