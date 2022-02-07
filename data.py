import pandas as pd
import csv

df = pd.read_csv("total_stars.csv")

#print(df)
#print(df.columns)


del df["Star"]
del df["distance"]
del df["mass"]
del df["radius"]
del df["Luminosity"]
del df["Unnamed: 0"]
del df["Unnamed: 6"]

print(list(df))

print(df)

df.to_csv('pro130.csv')