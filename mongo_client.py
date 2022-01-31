from pymongo import MongoClient

try:
    conn = MongoClient('mongodb://admin:admin@mongo-test', 27017)
    print("Connection Successful")
except:
    print("Connection Problem")


db = conn.test_db
collection = db.testTable

cursor = collection.find()
for record in cursor:
    print(record)