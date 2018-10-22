#!D:\Python\Python27
#!D:\Python\Python36
# -*- coding: UTF-8 -*-

num = 2
while num < 100:
	div = 2
	while div <= (num/div):
		if 0 == num % div:
			break
		div += 1
	else:
		print num
	num += 1