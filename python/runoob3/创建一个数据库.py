import pymongo
 
myclient = pymongo.MongoClient("mongodb://106.75.227.42:27017/")
mydb = myclient["runoob"]