import re

phone = '2004-959-559 # this is a outside phonenum'
print re.sub(r'#.*$', "", phone)
print re.sub(r'\D', "", phone)