import numpy as np
import scipy as sp
from statistics import mean

def SMA(values):    #for trend determination
    return mean(values)

def EMA(values):    #for BBands-range trading and also trend determination
    #Initial X-EMA = X-SMA where X is time period
    #   Initial X-SMA = mean(values) with X amounts of values
    #Multiplier = 2 / (X + 1)
    #EMA = (Close - prev_EMA) * Multiplier + prev_EMA
    return 0

def BBands(values): #for range-bound trading
    #upper band is EMA + stdev * multiplier
    #lower band is EMA -stdev * multiplier
    #20-EMA in the center
    return 0

def ADX_DMI(values): #to differentiate between range-bound and trendy markets

    return 0

