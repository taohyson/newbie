class Vector(object):
	"""docstring for Vector"""
	def __init__(self, a, b):
		super(Vector, self).__init__()
		self.a = a
		self.b = b

	def __str__(self):
		return '(%d %d)' % (self.a, self.b)

	def __add__(self, vector):
		return Vector(self.a + vector.a, self.b + vector.b)

u = Vector(10,20)
v = Vector(4, 2)

print u
print v
print u+v
