import ccxt
from datetime import datetime, timedelta, timezone
import math
import pandas as pd

# Using binance for altcoin data, base is BTC. Also kraken for BTC/EUR and ETH/EUR
exchanges = ['binance', 'kraken']
symbols = {
    'binance' : ['ETH/BTC', 'ADA/BTC', 'XMR/BTC', 'TRX/BTC', 'IOTA/BTC', 'ZEC/BTC', 'ICX/BTC', 'NANO/BTC', 'BAT/BTC', 'KMD/BTC'],
    'kraken' : ['BTC/EUR', 'ETH/EUR']
}
timeframes = ['1w', '1d', '4h']

for exchange in exchanges:
    _exchange = exchange
    exchange = getattr (ccxt, exchange) ()
    exchange.load_markets()
    for symbol in symbols[_exchange]:
        for timeframe in timeframes:
             # Get data
            data = exchange.fetch_ohlcv(symbol, timeframe)
             # Get UTC time from millisecond timestamp
            for index in range(0, len(data)):
                data[index][0] = str(datetime.fromtimestamp(data[index][0] / 1000))
            header = ['Datetime', 'Open', 'High', 'Low', 'Close', 'Volume']
            df = pd.DataFrame(data, columns=header)
            df.set_index('Datetime', inplace=True)
             # Save it
            symbol_out = symbol.replace("/","")
            filename = '{}-{}-{}.csv'.format(_exchange, symbol_out, timeframe)
            df.to_csv(filename)