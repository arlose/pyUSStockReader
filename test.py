# importing the necessary packages
# following the tutorial from pythonprogramming.net

# https://pydata.github.io/pandas-datareader/devel/remote_data.html#

import pandas as pd 
import datetime as dt 
import pandas_datareader.data as web
import matplotlib.pyplot as plt 
from matplotlib import style


style.use('ggplot') # Setting the style of our plots

start = dt.datetime(2015, 1, 1)  # The start date for our data

end = dt.datetime(2017, 12, 31) # The ending date for our data 

# Create a pandas DataFrame for the Tesla company grabbing from Yahoo
# df = web.DataReader('TSLA', 'yahoo', start, end)
'''
from pandas_datareader import data, wb

import pandas_datareader as pdr
aa = pdr.get_data_fred('GOOG')

print aa
'''

# f = web.DataReader('GOOG', 'iex', start, end)
# print f

# f = web.DataReader('GOOG', 'robinhood', start, end)
# print f

f = web.DataReader('JD', 'morningstar', start, end)
print f.head()
