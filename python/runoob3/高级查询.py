import pymongo

c = pymongo.MongoClient("mongodb://106.75.227.42:27017/runoob")
db = c['runoob']
col = db['sites']

for x in col.find({ "name": { "$gt": "H" } }):
	print(x)
print()

for x in col.find({ "name": { "$regex": "^R" } }):
	print(x)
print()