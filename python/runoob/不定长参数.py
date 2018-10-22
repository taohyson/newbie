def function(argc, *argv):
	print argc
	for arg in argv:
		print arg
	pass

function(1)
function(10,20,30,40)