import backtrader as bt
import backtrader.feeds as btfeeds
import backtrader.indicators as btind
from datetime import datetime, timedelta, timezone
import matplotlib

class Sizer_for_BollBands(bt.Sizer):

    params = (
        ('risk', 0.02),
    )

    def _getsizing(self, comminfo, cash, data, isbuy):
        if isbuy == True:
            size = (self.params.risk * cash) / (self.data.close[0] - self.data.low[-1])
        else:
            size = (self.params.risk * cash) / (self.data.close[0] - self.data.low[-1]) * -1
        return size

class MeanReversionStrategy(bt.Strategy):

    params = (
        ('BBperiod', 20),
        ('devfactor', 2),
        ('stopfactor', 0.01),
        ('entryfactor', 0.01),
        ('targetfactor', 0.02),
    )

    def __init__(self):

        self.bbands = btind.BBands(self.data0, period=self.params.BBperiod, devfactor=self.params.devfactor)
        self.stdev =  btind.StandardDeviation(self.data0, period=self.params.BBperiod)

    def next(self):

        if not self.position:
            
            # touching upper band, creating a sell bracket order
            if self.data.close[-1] > self.bbands.top[-1] and self.data.close[0] < self.bbands.top[0]:

                stop = self.data.high[-1] + self.stdev * self.params.stopfactor
                entry = self.data.close[0] - self.stdev * self.params.entryfactor
                target = self.bbands.mid[0] + self.stdev * self.params.targetfactor

                short_bracket = self.sell_bracket(stopprice=stop, price=entry, limitprice=target)

            # touching lower band, creating a buy/ bracket order
            if self.data.close[-1] < self.bbands.bot[-1] and self.data.close[0] < self.bbands.bot[0]:

                stop = self.data.low[-1] - self.stdev * self.params.stopfactor
                entry = self.data.close[0] + self.stdev * self.params.entryfactor
                target = self.bbands.mid[0] - self.stdev * self.params.targetfactor

                long_bracket = self.buy_bracket(stopprice=stop, price=entry, limitprice=target)


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

cerebro.addstrategy(MeanReversionStrategy)

cerebro.adddata(data)
cerebro.broker.setcash(400.0)

cerebro.addsizer(Sizer_for_BollBands)
# Print out the starting conditions
print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

# Run over everything
cerebro.run()

# Print out the final result
print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())

# Plot the result
cerebro.plot()
