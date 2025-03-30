import pandas as pd
from pymongo.mongo_client import MongoClient
import json
import pandas as pd
from pymongo.mongo_client import MongoClient

# MongoDB connection details
url = "mongodb+srv://shubham:9012885070@cluster0.jcwkp.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
DATABASE_Name = "sensor-project"
Collection_name = "waferfault"

# Fetch data from MongoDB
df=pd.read_csv("F:\project-sensor-fault-detection\notebook\wafer_23012020_041211.csv")
df=df.drop("Unnamed: 0",axis=1)
json_record=list(json.loads(df.T.to_json()).values())
client[DATABASE_Name][Collection_name].insert_many(json_record)
