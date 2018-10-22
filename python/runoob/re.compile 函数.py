import re
pattern = re.compile(r'\d+')
m = pattern.match('one12twothree34four')
print m
m = pattern.match('one12twothree34four', 2, 10)
print m
m = pattern.match('one12twothree34four', 3, 10)
print m
print m.group(0)
print m.start(0)
print m.end(0)
print m.span(0)
