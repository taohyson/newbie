#!D:\Python\Python27

def queen(A, cur=0):
	if cur == len(A):
		print A
		return 0
	for col in range(len(A)):
		A[cur],flag = col+1,True
		for row in range(cur):
			if A[cur] == A[row] or abs(A[cur] - A[row]) == (cur - row):
				flag = False
				break;
		if flag:
			queen(A, cur + 1)

queen([None]*8)