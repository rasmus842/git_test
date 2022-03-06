
# Accessing data feeds:
# self.data     targets     self.datas[0]
# self.dataX    targets     self.datas[X]
# Note: almost anything can be a data feed. for every instance of data you can calculate new data feed objects



# params either a tuple or a dictionary
# params = (('period', 20),)
# params = dict(period=20)
# Accessing params values later on:
# self.params.period    or shorthand    self.p.period


# Lines. Mostly every other object is a .lines enabled.
# For data feeds you can use shorter version which is more natural. You use the longer version when dealing with indicators
# self.close[0]    points to   self.lines.close[0]

# Shorthand access to lines do exist:
# x.lines    can be shortened to     x.l
# x.lines.name       can be shortened to     x.lines_name

# Complex objects like Strategies and Indicators offer quick access to data’s lines
# self.data_name    offers a direct access to   self.data.lines.name
# Which also applies to the numbered data variables: self.data1_name -> self.data1.lines.name

# Additionally the line names are directly accessible with:
# self.data.close   and     self.movav.sma
# But the notation doesn’t make as clear as the previous one if lines are actually being accessed.
#

# If you are developing your own indicator then you have to declare which lines it has
# class SimpleMovingAverage(Indicator):
#     lines = ('sma',)
#     ...

# Delayed lines
# defining a condition or a line object in the init phase rather than doing it over and over again in next
# when comparing different time frames


# to access previous values of a data feed or lines object
# ago = the starting point, default is 0, size is the amount of values to get
# .get(ago=0, size=1)

# bt.And(statement0, statement1) etc, returns boolean
# bt.If(statement, value_if_True, value_if_False)


# More can be done with other Strategy classes:

# buy / sell / close    -   Use the underlying broker and sizer to send the broker a buy/sell order

# The same could be done by manually creating an Order and passing it over to the broker. But the platform is about making it easy for those using it.

# close will get the current market position and close it immediately.

# getposition (or the property “position”)  -   Returns the current market position

# setsizer/getsizer (or the property “sizer”)   -   These allow setting/getting the underlying stake Sizer. The same logic can be checked against Sizers which provide different stakes for the same situation (fixed size, proportional to capital, exponential)