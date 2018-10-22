class testself(object):
	"""docstring for testself"""
	def __init__(self):		
		print self
		print self.__class__
		print self.__init__

t = testself()