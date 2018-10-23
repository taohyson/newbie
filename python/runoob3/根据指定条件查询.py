import pymongo

c = pymongo.MongoClient("mongodb://106.75.227.42:27017/runoob")
db = c['runoob']
col = db['sites']
for x in col.find({'name':'zx'}):
	print(x)