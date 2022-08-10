import requests
import time

while True:
    def precioBTC():
        f = open('BTC.txt', 'r')
        precio = f.read()

        x = precio.split("/")
        precioF = float(x[0])
        print(f'BTC: {round(precioF, 2)}€')
        f.close()

    def precioETH():
        f = open('ETH.txt', 'r')
        precio = f.read()

        x = precio.split("/")
        precioF = float(x[0])
        print(f'ETH: {round(precioF, 2)}€')
        f.close()


    headers = {
            'X-CMC_PRO_API_KEY': '[API-KEY]',
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
            file = open("./BTC.txt","w")
            file.write(str(round(coin['quote']['EUR']['price'],5) ) + "\n" )
            file.close();
        if coin['symbol'] == 'ETH':
            file = open("./ETH.txt","w")
            file.write(str(round(coin['quote']['EUR']['price'],5) ) + "\n" )
            file.close();

    precioBTC()
    precioETH()

    time.sleep(60)






