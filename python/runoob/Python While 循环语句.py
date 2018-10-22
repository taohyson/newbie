#!D:\Python\Python27
#!D:\Python\Python36
# -*- coding: UTF-8 -*-

count = 0
while (count < 9):
	print count
	count += 1

count = 10
while count < 19:
	if 16 == count:
		break
	else:
		count += 1
	if 0 == count % 2:
		continue
	else:
		print count

count = 20
while count < 29:
	count += 1
else:
	print count