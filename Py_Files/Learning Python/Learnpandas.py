import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
import numpy as np

#   NUMPY
#np.array(list) gives a numpy array for us to do some shit with
#df.values drops the indeces and headers and just gives us the numerical data

#   PANDAS BASICS - the dataframe structure - behaves like a dictionary, 0th column is the index column
#df = pd.DataFrame(data, source, start, end)
#df.set_index(key, inplace=True) - inplace=true to modify , else you have to assign to a variable
#df.reset_index(inplace=True) - the old index is modified into a column
# df[key].tolist  - aswell
#np.array(list) - to an array with NumPy
#df.columns = ['1st name', 2nd name'] etc - change the name of the column
#df.rename(columns = ['existing name': 'new name', inplace=True] - can rename one column

#   IO BASICS IN PANDAS - Can use to convert data formats aswell. E.g. csv to excel
#df = pd.read_csv('name.csv', index_col=0) or any other file name .html .excel etc
#or read_csv('name.csv', parse_dates=True)
#output = df.to_csv('name.csv')
#df.to_csv('name.csv', header=False) no column names
#df = pd.read.csv('name.csv', names=['Dates', 'colname', index_col=0])
#   PICKLING - reading lots of data from the internet and quickly writing it down to a file
#pickle_out = open('name.pickle', 'wb')
#pickle.dump(df, pickle_out)
#pickle_out.close()
#pickle_in = open('name.pickle', 'rb')
#data = pickle.load(pickle_in)
#OR USING PANDAS PICKLING SYNTAX with just 2 lines of code
#df.to_pickle('name.pickle')
#df2 = pd.read_pickle('name.pickle')

#reading from websites with pd.read.html gets you a LIST of dataframes that are in the website.

#   DATA ANALYSIS FUNCTIONS
#df = df.pct_change()
#calculates the change of the last and current values for every number
#   CORRELATION
#df_correlation = df.corr() 
#this gives us a correlation table
#df_correlation.describe() 
#stat data. The values should be of similar type. E.g. percent change
#   RESAMPLING THE DATA
#weekly_df = df.resample['resample by what', how=mean] 
#resampling, e.g. daily data to weekly, minute data to daily etc
#   ROLLING STATISTICS
#df[key_xMA] = pd.rolling_mean(df[key], x)
#basically calculating the simple moving average
#   STANDARD DEVIATION
#df[key_xstd] = pd.rolling_std(df[key], x)
#calculates the std deviation of the last x data points
#   ROLLING CORRELATION
#pd.rolling_corr(df[key1], df[key2])
#and others aswell
#   ROLLING_APPLY
#df[key_x-SMA] = df.rolling_apply(key, x, SMA)
#where SMA is a function that accepts a list of values and returns the mean of them

#   COMPARISON OPERATORS IN DATAFRAMES
#df = df[ (df['std'] < df_std) ]
#If a row does not meet this criteria then it is removed from the dataset
#Can be used to remove erronious data

#   PREDICTING FUTURE VALUES
#df[key_future] = df[key].shift(-1)


#   CONCATENATION, ADDING
#   CONCAT
#concat = pd.concat([df1, df2, df2]) etc
#df4 = df1.append(df2) adds df2 to the end of df1
#   APPEND
#can create series and add that to a dataframe. But not effective
#s = pd.series([1, 3, 2], index = [key1, key2, key3]) like a new row to be added to a database
#pd4 = pd1.append(s, ignore_index=True)
#   MERGING, JOINING
#   MERGING
#merging: merged = pd.merge(df1, df2, on='index' how='right') where how = left, right (df1 or df2), outer(all indeces), inner()
#need to set index again with merged.set_index(index, inplace=True)
#   Joining

#   MISSING DATA HANDLING.
#   Option1 - ignore and do nothing
#   Option 2 - delete the missing data row
#df.dropna(inplace=True) - deletes NaN from df
#can also use how='all' if you only want to drop columns that have all NaN's in them
#threshhold parameter
#   Option 3 - fill in the missing data with a preceding or future number, or an averaged number
#df.fillna(method='ffill', inplace=True) 
#forwardfill = 'ffill' or backfill = 'bfill' OR value = a determined value
#limit parameter and df.isnull().values.sum() to calculate how many NaN's we have
#   Option 4 - replace the missing data with a static number
#df.replace([list of values], value, inplace=True)

#   SKLEARN and MACHINE LEARNING
#from sklearn import svm, preprocessing, cross_validation
#X = np.array(housing_data.drop(['label','US_HPI_future'], 1))
#X = preprocessing.scale(X)
#   X are features. You want to drop the series that are going to be lables
#y = np.array(housing_data['label'])
#   labels are the values that machine learning uses to test itself
#X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)
#   split up training and testing sets
#clf = svm.SVC(kernel='linear') - establishing a classifier. a linear kernel
#clf.fit(X_train, y_train) - training the classifier
#print(clf.score(X_test, y_test)) - printing the scores
#   establishing a classifier

df = pd.DataFrame()

#set the index if not already set
df.set_index('key', inplace=True) #Set the key, inplace=true means that it modifies the dataframe in the variable df, usually it just returns another dataframe
#or df = df.set_index('key')

#referencing a specific column
print(df['key'])
#or
print(df.Key) # If the key is without whitespace
#Referencing more columns at once
print(df[['key1', 'key2']])

#Putting the data into a python list
print(df.Key.tolist())
#How to put multiple columns into a list. You need to an array beforehand with numpy
print(np.array(df[['key1', 'key2']]))

#Can create another dataframe from the created array
df2 = pd.DataFrame(np.array(df[['key1', 'key2']]))



