import pandas_datareader.data as pdr
import yfinance as yf
yf.pdr_override()

df = pdr.get_data_yahoo('AAPL', start='2023-01-01', end='2024-03-15').reset_index()
df['Ticker'] = 'AAPL'
df = df[['Ticker','Date','Close']]

print(df)
