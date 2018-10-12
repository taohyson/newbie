#!D:\Python\Python27

count = 0

while count < 10:
	count += 1
	if count % 2 == 1:
		continue
	if count == 10:
		break
	print count
else:
	print count