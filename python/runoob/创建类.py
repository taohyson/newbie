class Employee(object):
	"""docstring for Employee"""
	count = 0
	def __init__(self, name, salary):		
		self.name = name
		self.salary = salary
		Employee.count += 1

	def total(self):
		print Employee.count

	def info(self):
		print self.name
		print self.salary

e = Employee('zx',10*1024)
e.total()
e.info()