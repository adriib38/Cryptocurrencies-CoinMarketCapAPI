import requests
import time

headers = {
        'X-CMC_PRO_API_KEY': '0914e058-72b9-46fd-b1e2-7c5b0659c564',
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

        btc =	{

        }
        
        btc["live"] = round(coin['quote']['EUR']['price'])
        btc["last_updated"] = coin['quote']['EUR']['last_updated']

        print(btc)

#DOCU: https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyListingsLatest
