import pymongo

class Point(object):
	"""docstring for Point"""
	def __init__(self, x, y):
		super(Point, self).__init__()
		self.x = x
		self.y = y

c = pymongo.MongoClient("mongodb://106.75.227.42:27017/")
db = c['runoob']
col = db['sites']
ins = col.insert_one(Point(10, 20).__dict__)
print ins.inserted_id