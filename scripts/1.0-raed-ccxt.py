import os
import sys
import time
import csv
from pprint import pprint
import ccxt  # noqa: E402


root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root + '/python')

f = open("/Users/raedzorkot/Desktop/Workbook1.csv", "w")
f.truncate()
f.close()
id = ["bitstamp", "kraken", "bitfinex"]
for id1 in id:
# instantiate the exchange by id
    exchange = getattr(ccxt, id1)({
                                 # 'proxy':'https://cors-anywhere.herokuapp.com/',
                                 })

# load all markets from the exchange
    markets = exchange.load_markets()



    m=[]
    ex=['ETH/BTC', 'LTC/BTC'] ## add the coins symbol you want
    delay = 2 # seconds
    for symbol in ex: ## change ex to exchange if you want it to iterate through all the coins
        print('-------------------------------------------')
        print(symbol.split(" "))
    
        c=exchange.fetch_order_book(symbol)

        with open('/Users/raedzorkot/Desktop/Workbook1.csv', 'a') as csvfile:
            fieldnames = [id1, symbol, 'asks', 'bids', 'datetime', 'nonce', 'timestamp']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            writer.writerow(c)







