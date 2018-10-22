#!D:\Python\Python27
#!D:\Python\Python36
# -*- coding: UTF-8 -*-
from __future__ import print_function

for letter in 'Python':
	if 'h' == letter:
		continue
	print(letter, end="")

for num in range(10):
	if 4 == num:
		continue
	else:
		print(num, '\t', end="")
