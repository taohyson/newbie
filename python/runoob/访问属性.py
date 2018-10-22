class Employee():
	"""docstring for Employee"""
	def __init__(self):
		pass

	def fun1(self, name, age, salary):
		# super(Employee, self).__init__()
		self.name = name

e1 = Employee()
e1.name = 'xx'
e1.age = 18
e2 = Employee()
e2.name = 'yy'
e2.salary = 10*1024

print getattr(e1,"age")
print hasattr(e1, "salary")
setattr(e1,"age",20)
print getattr(e1,"age")
delattr(e1, "age")
		