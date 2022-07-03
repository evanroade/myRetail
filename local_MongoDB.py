import pymongo
from pymongo import MongoClient

connection_string = "mongodb://127.0.0.1:27017"
client = MongoClient(connection_string)
db = client["myRetail"]
collection = db["pricing"]

post1 = {"_id":13860428, "value":13.49, "currency":"USD"}
post2 = {"_id":54456119, "value":33.55, "currency":"USD"}
post3 = {"_id":13264003, "value":20.25, "currency":"USD"}
post4 = {"_id":12954218, "value":10.15, "currency":"USD"}
post5 = {"_id":35645454, "value":59.99, "currency":"USD"}

collection.insert_many([post1, post2, post3, post4, post5])


