import pandas as pd
pd.options.mode.chained_assignment = None

df = pd.read_csv("../data/SuperStore2024.csv")
df = df[['Row ID','Customer Name','Sales','Profit']]
df['Cost'] = df['Sales'] - df['Profit']

print(df)
