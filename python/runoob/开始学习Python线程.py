import thread
import time

def func(name, delay):
	count = 0
	while count < 5:
		time.sleep(delay)
		count += 1
		print "%s %s" % (name, time.ctime(time.time()))

try:
	thread.start_new_thread(func,('th-1',2))
	thread.start_new_thread(func,('th-2',4))
except Exception as e:
	print e

while True:
	pass