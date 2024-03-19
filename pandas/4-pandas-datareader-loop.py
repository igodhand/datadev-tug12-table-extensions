import pandas as pd
import pandas_datareader.data as pdr
import yfinance as yf
yf.pdr_override()

tickers = ['AAPL', 'GOOG', 'CRM']

df = pd.DataFrame()

for ticker in tickers:
    df_temp = pdr.get_data_yahoo(ticker, start='2023-01-01', end='2024-03-15').reset_index()
    df_temp['Ticker'] = ticker
    df_temp = df_temp[['Ticker', 'Date', 'Close']]
    df = df._append(df_temp)

print(df)
