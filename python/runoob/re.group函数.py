import re

line = 'cats are smarter than dogs'

mt = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
if mt:
	print mt.group()
	print mt.group(1)
	print mt.group(2)
else:
	print 'nothing'

