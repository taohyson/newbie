import pymongo

c = pymongo.MongoClient("mongodb://106.75.227.42:27017/")
db = c['runoob']
col = db['sites']
col.update_one({'name':'zx'},{'$set':{'name':'zjw'}})
up = col.update_many({ "name": '{ "$regex": "^F" }' },{'$set':{'name':'zx'}})
print(up.modified_count)