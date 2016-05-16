import statsmodels.tsa.stattools as ts
import pandas
from datetime import datetime
import matplotlib.pyplot as plt
from pandas_datareader.data import DataReader as webdata
from ggplot import *
import warnings
warnings.filterwarnings("ignore")


#matplotlib.style.use('ggplot')

ford = webdata("F", "yahoo", datetime(2000,1,1), datetime(2016,4,21))
#print(ford.tail())
#print(type(ford))
faclose = ford['Adj Close']
#print((faclose))
faclose.plot()
plt.show()
