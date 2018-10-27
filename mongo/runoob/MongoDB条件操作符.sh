db.col.find({"likes":{"$gt" : 100}})
db.col.find({"likes":{"$gte" : 100}})
db.col.find({"likes":{"$lt" : 150}})
db.col.find({"likes":{"$gt": 100, "$lt" : 150}})
