import datetime as dt
import pandas as pd
import quandl
import numpy as np

quandl.ApiConfig.api_key = '1QJMds64iWZ9mQZ81_se'

end = dt.datetime.now()
start = dt.datetime(2018, 1, 1)

df = quandl.get("GDAX/ETH_EUR")

print(df.tail())