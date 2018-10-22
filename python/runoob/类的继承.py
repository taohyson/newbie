class Base(object):
	"""docstring for Base"""
	def __init__(self):
		super(Base, self).__init__()

	def pubfun(self):
		print 'public base function'

	def basefun(self):
		print 'base function'

class Derived(Base):
	"""docstring for Derived"""
	def __init__(self):
		super(Derived, self).__init__()

	def pubfun(self):
		print 'public derived function'
					
d = Derived()
d.name = 'zx'
d.pubfun()
d.basefun()