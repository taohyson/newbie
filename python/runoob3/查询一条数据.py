import pymongo

c = pymongo.MongoClient("mongodb://106.75.227.42:27017/runoob")
db = c['runoob']
col = db['sites']
print(col.find_one())
print()

for x in col.find():
	print(x)
print()

for x in col.find({'name':'zx'}):
	print(x)