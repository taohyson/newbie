import pymongo

c = pymongo.MongoClient("mongodb://106.75.227.42:27017/")
print 'runoob' in c.list_database_names()