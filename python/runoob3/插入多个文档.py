import pymongo
from TestPoint import TestPoint

c = pymongo.MongoClient("mongodb://106.75.227.42:27017/")
db = c['runoob']
col = db['sites']
objs = [
	TestPoint(1,2).__dict__,
	TestPoint(3,4).__dict__,
	TestPoint(5,6).__dict__,
	TestPoint(7,8).__dict__,
	TestPoint(9,0).__dict__
]
ins = col.insert_many(objs)
print ins.inserted_ids