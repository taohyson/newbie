try:
	fd = open("IOError", "w")
	fd.write("Hello")
except IOError as e:
	print "IOError"
else:
	print "OK"
	fd.close()