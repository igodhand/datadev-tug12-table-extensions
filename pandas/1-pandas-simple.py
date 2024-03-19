import pandas as pd

df = pd.read_csv("../data/SuperStoreSimple.csv")
df['Cost'] = df['Sales'] - df['Profit']

print(df)
