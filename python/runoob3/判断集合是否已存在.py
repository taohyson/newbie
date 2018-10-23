import pymongo

c = pymongo.MongoClient("mongodb://106.75.227.42:27017/")
db = c['runoob']
print 'sites' in db.list_collection_names()
print db.list_collection_names()