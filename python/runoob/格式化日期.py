#!D:\Python\Python27
#!D:\Python\Python36
# -*- coding: UTF-8 -*-

import time

print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())
str = "Sat Mar 28 12:00:00 2018"
print time.mktime(time.strptime(str, '%a %b %d %H:%M:%S %Y'))