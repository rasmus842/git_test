import backtrader as bt
import backtrader.feeds as btfeeds
import backtrader.indicators as btind
from datetime import datetime, timedelta, timezone
import matplotlib
from MyIndicators import MidTermHighs, MidTermLows

class Sizer_for_TrendTrading(bt.Sizer):
    
    params = (
        ('risk', 0.02),
    )

    # when shorting         stop = self.data.high[short_term_highs[i][0]] * 1.01
    #                       entry = self.data.close[short_term_highs[i + 1][0]] * 0.99

    # when longing          stop = self.data.low[short_term_lows[i][0]] * 0.99
    #                       entry = self.data.close[short_term_lows[i + 1][0]] * 1.01
    
    def _getsizing(self, comminfo, cash, data, isbuy):
        position = bt.strategy.getposition(data)
        if position.size > 0:
            if not isbuy:
                #reverse a long to a short position with the same size
                size = position.size * 2
        elif position.size < 0:
            if isbuy:
                #reverse a short to a long position with the same size
                size = position.size * 2
        else:
            # not in a position yet
            size = (self.params.risk * cash) / 

        return size

class TrendTrading(bt.Strategy):

    # def __init__(self):
    #     adx of larger timeframe, if adx high enough I will trigger an order
    #     dmi or sma for further conditions regarding which direction to trade in

    def once(self, start, end):

        highs = self.highs.array
        short_term_highs = []
        mid_term_highs = []
        mid_term_highs_indeces = []

        lows = self.lows.array
        short_term_lows = []
        mid_term_lows = []
        mid_term_lows_indeces = []

        if len(highs) > 2:
            for i in range(1, end - 1):
                if highs[i] > highs[i - 1] and highs[i] > highs[i + 1]:
                    short_term_highs.append([i, highs[i]])
        else:
            raise bt.StrategySkipError

        if len(lows) > 2:
            for i in range(1, end - 1):
                if lows[i] < lows[i - 1] and lows[i] < lows[i + 1]:
                    short_term_lows.append([i, lows[i]])
        else:
            raise bt.StrategySkipError

        
        if len(short_term_highs) > 2:
            for i in range(1, len(short_term_highs) - 1):
                if short_term_highs[i][1] > short_term_highs[i - 1][1] and short_term_highs[i][1] > short_term_highs[i + 1][1]:
                    mid_term_highs.append(short_term_highs[i])
                    mid_term_highs_indeces.append(short_term_highs[i][0])
        else:
            raise bt.StrategySkipError

        if len(short_term_lows) > 2:
            for i in range(1, len(short_term_lows) - 1):
                if short_term_lows[i][1] < short_term_lows[i - 1][1] and short_term_lows[i][1] < short_term_lows[i + 1][1]:
                    mid_term_lows.append(short_term_lows[i])
                    mid_term_lows_indeces.append(short_term_lows[i][0])
        else: 
            raise bt.StrategySkipError


        # now to trigger orders based on intermediate term highs and lows:

        for i in range(end - 1):

            if 

            elif i in mid_term_highs_indeces:
                position = bt.position()
                stop_price = self.data.high[short_term_highs[i][1]] * 1.01
                entry_price = self.data.close[short_term_highs[i + 1][1]] * 0.99
                # no targets in this system

                if position.size > 0:
                    # reverse the position
                    self.cancel(stop_order)
                    short_order = self.sell(self.datas[i + 1], price=entry_price, exectype=Order.Limit, valid=0)
                    stop_order = self.buy(self.datas[i + 1], price=stop_price, exectype=Order.Stop)
                elif position.size < 0:
                    # update the stop order
                    self.cancel(stop_order)
                    stop_order = self.buy(self.datas[i + 1], price=stop_price, exectype=Order.Stop)
                else:   
                    #no positions
                    short_order = self.sell(self.datas[i + 1], price=entry_price, exectype=Order.Limit, valid=0)
                    stop_order = self.buy(self.datas[i + 1], price=stop_price, exectype=Order.Stop)


                
            elif i in mid_term_lows_indeces:
                position = bt.position()
                stop_price = self.data.low[short_term_lows[i][1]] * 0.99
                entry_price = self.data.close[short_term_lows[i + 1][1]] * 1.01

                if position.size > 0:
                    # update the stop order
                    self.cancel(stop_order)
                    stop_order = self.sell(self.datas[i + 1], price=stop_price, exectype=Order.Stop)
                elif position.size < 0:
                    # reverse the position
                    self.cancel(stop_order)
                    long_order = self.buy(self.datas[i + 1], price=entry_price, exectype=Order.Limit, valid=0)
                    stop_order = self.sell(self.datas[i + 1], price=stop_price, exectype=Order.Stop)
                else:
                    #no positions
                    long_order = self.buy(self.datas[i + 1], price=entry_price, exectype=Order.Limit, valid=0)
                    stop_order = self.sell(self.datas[i + 1], price=stop_price, exectype=Order.Stop)





csv_file = 'kraken-ETHEUR-1d.csv'
# Something like this is aslo possible
# data = bt.BacktraderCSVData(dataname='mypath.days', timeframe=bt.TimeFrame.Days)
data = btfeeds.GenericCSVData(
    dataname=csv_file,

    # fromdate=     # default = mindate
    # todate=       # default = maxdate

    # nullvalue=0.0,    the value which will be used if there is a value that is not found,  default is NaN

    # dtformat=     # default = %Y-%m-%d %H:%M:%S
    # tmformat=     # default = %H:%M:%S

    # datetime=     # default = 0
    # time=         # default = -1
    # open=         # default = 1
    # high=         # default = 2
    # low=          # default = 3
    # close=        # default = 4
    # volume=       # default = 5
    # openinterest= # default = 6
    openinterest=-1
)
cerebro = bt.Cerebro()

cerebro.addstrategy(TrendTrading)

cerebro.adddata(data)
cerebro.broker.setcash(10000)

cerebro.addsizer(Sizer_for_TrendTrading)

print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

cerebro.run()

print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())

# Plot the result
cerebro.plot()