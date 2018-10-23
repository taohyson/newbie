import json

class TestPoint(object):
	"""docstring for TestPoint"""
	def __init__(self, x, y):
		super(TestPoint, self).__init__()
		self.x = x
		self.y = y
	def __str__(self):
		return json.dumps(self.__dict__, indent = 4, sort_keys = True)

if __name__ == '__main__':
	pt = TestPoint(10, 20)		
	print pt