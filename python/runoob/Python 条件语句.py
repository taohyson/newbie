#!D:\Python\Python27
#!D:\Python\Python36
# -*- coding: UTF-8 -*-

name = 'john'
if name == 'Python':
	print 'boss'
else:
	print name

num = 5
if 3 == num:
	print 'boss'
elif 2 == num:
	print 'user'
elif 1 == num:
	print 'worker'
elif 0 >= num:
	print 'error'
else:
	print 'stranger'

num = 10
if 0 <= num and num <= 10:
	print 'hello'
if num < 0 or 10 < num:
	print 'inner' 
else:
	print 'outer'
if (0 <= num and num <= 5) or (10 <= num and num <=15):
	print 'bound'