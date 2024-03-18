import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
pd.options.mode.chained_assignment = None

df = pd.read_csv("../data/SuperStore2024.csv")
df = df[['Row ID','Customer Name','Sales','Profit']]

scaler = MinMaxScaler()
columns= ['Sales', 'Profit']
df[columns] = scaler.fit_transform(df[columns])

kmeans = KMeans(n_clusters=5, random_state=42)
features = df[['Sales', 'Profit']]
kmeans.fit(features)
df['Cluster'] = kmeans.labels_

print(df)
