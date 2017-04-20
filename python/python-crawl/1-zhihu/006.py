# mongodb的使用
from pymongo import MongoClient

client = MongoClient()
print(client.database_names())