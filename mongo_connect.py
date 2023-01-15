from pymongo import MongoClient
import csv
import pandas as pd
import json

client = MongoClient('localhost', 27017)
df = pd.read_csv('ekanshi.csv')
data= df.to_dict(orient="records")
reddit_data = client["test_mongo"]["data"]
print(data)
reddit_data.insert_many(data)