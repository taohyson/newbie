import pymongo

c = pymongo.MongoClient("mongodb://106.75.227.42:27017/")
db = c['runoob']
col = db['sites']
col.delete_one({'name':'zjw'})
de = col.delete_many({'name':'zjw'})
print (de.deleted_count)