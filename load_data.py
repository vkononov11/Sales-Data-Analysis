import sqlite3
import pandas as pd


conn = sqlite3.connect("database/sales.db")

df = pd.read_csv("data/sales.csv")

df.columns = (
    df.columns
    .str.lower()
    .str.replace(" ", "_")
    .str.replace("/", "_")
    .str.replace("-", "_")
)

with open("database/create_tables.sql", "r") as file:
    sql_script = file.read()

conn.executescript(sql_script)

df.to_sql("sales", conn, if_exists="append", index=False)

print("Data loaded successfully!")

print(df.shape)

conn.close()