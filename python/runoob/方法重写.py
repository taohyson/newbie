class Base(object):
	"""docstring for Parent"""
	def overfunc(self):
		print 'Base func'

class Derived(Base):
	"""docstring for Derived"""
	def overfunc(self):		
		print 'Derived func'

d = Derived()
d.overfunc()