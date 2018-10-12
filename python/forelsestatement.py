#!D:\Python\Python27

for num in range(10,100):
	for i in range(2, num / 2):
		if num % i == 0:
			break
	else:
		print num
