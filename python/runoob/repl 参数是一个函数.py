import re

def double(matched):
	value = int(matched.group('value'))
	return str(value * 2)

s = 'A273DEIF02'
print re.sub('(?P<value>\d+)', double, s)