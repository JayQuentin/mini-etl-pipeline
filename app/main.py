import pandas as pd
import sqlite3

# EXTRACT: Load CSV

csv_file = "data/titanic_test.csv"
df = pd.read_csv(csv_file)

# TRANSFORM: Clean Data
df.dropna(inplace=True) # Delete missing values

# LOAD: Save in SQLite Database
conn = sqlite3.connect("data/database.db")
df.to_sql("titanic", conn, if_exists="replace", index=False)
conn.close()

print("ETL process done. Data saved in Database")