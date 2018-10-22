import re
print re.split('\W+', 'runoob, runoob, runoob.')
print re.split('(\W+)', ' runoob, runoob, runoob.') 
print re.split('\W+', ' runoob, runoob, runoob.', 1) 
print re.split('a*', 'hello world')
