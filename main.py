import requests
import time

headers = {
        'X-CMC_PRO_API_KEY': 'YOUR-API-KEY',
        'Accepts': 'application/json'
        }

params = {
        'start': '1',
        'limit': '6',
        'convert': 'EUR'
        }

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

json = requests.get(url, params = params, headers = headers).json()

coins = json["data"]
#print(coin)

for coin in coins:
      #print(coin['symbol'])
      #print(round(coin['quote']['EUR']['price'],5))
    
      if coin['symbol'] == 'BTC':
        #print(coin['symbol'])
        #print(round(coin['quote']['EUR']['price'],5))

        btc["name"] = coin["name"]
        btc["live"] = round(coin['quote']['EUR']['price'])
        btc["last_updated"] = coin['quote']['EUR']['last_updated']
        btc["percent_change_1h"] = coin['quote']['EUR']['percent_change_1h']
        btc["percent_change_24h"] = coin['quote']['EUR']['percent_change_24h']
        btc["percent_change_7d"] = coin['quote']['EUR']['percent_change_7d']

        for clave in btc:
          # Hacer algo con esa clave
          print(clave)
          valor = btc[clave]
          print(valor)

#DOCU: https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyListingsLatest
