def make_int_list(x):
	l = [int(e) for e in x.split()]
	return l
	
def is_odd(e):
	if e%2==0:
		return False
	else:
		return True
		
def odd_list(alist):
	l = []
	for i in range(len(alist)):
		if alist[i]%2!=0:
			l.append(alist[i])
	return l

def sum_square(alist):
	sum = 0
	for i in range(len(alist)):
		sum+= alist[i]**2
	return sum
exec(input().strip())
	
	