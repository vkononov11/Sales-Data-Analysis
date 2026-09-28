import pandas as pd

df = pd.read_csv("data/sales.csv")

df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Order Date"])

df.info()