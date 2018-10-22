class Point(object):
	"""docstring for Point"""
	def __init__(self, x=0,y=0):
		super(Point, self).__init__()
		self.x = x
		self.y = y

	def __del__(self):
		print self.__class__.__name__

p1 = Point()
p2 = p1
p3 = p2
print id(p1)
print id(p2)
print id(p3)
del p1
del p2
del p3