#!D:\Python\Python27
#!D:\Python\Python36
# -*- coding: UTF-8 -*-

for num in range(10,20):
	for div in (2,num//2):
		if 0 == num%div:
			break
	else:
		print(num)