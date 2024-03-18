import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yfin
yfin.pdr_override()

df1 = pdr.get_data_yahoo('AAPL', start='2023-01-01', end='2024-03-15').reset_index()
df1['Ticker'] = 'AAPL'
df1 = df1[['Ticker','Date','Close']]

df2 = pdr.get_data_yahoo('GOOG', start='2023-01-01', end='2024-03-15').reset_index()
df2['Ticker'] = 'GOOG'
df2 = df2[['Ticker','Date','Close']]

df3 = pdr.get_data_yahoo('CRM', start='2023-01-01', end='2024-03-15').reset_index()
df3['Ticker'] = 'CRM'
df3 = df3[['Ticker','Date','Close']]

df = pd.concat([df1, df2, df3])

df['Date'] = df['Date'].astype(str)

print(df)
