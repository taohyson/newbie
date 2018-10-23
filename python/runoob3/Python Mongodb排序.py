import pymongo

c = pymongo.MongoClient("mongodb://106.75.227.42:27017/")
db = c['runoob']
col = db['sites']
for x in col.find().sort('name'):
	print (x)
for x in col.find().sort('name',-1):
	print (x)