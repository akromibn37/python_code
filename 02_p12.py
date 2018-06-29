ca,a = [int(e) for e in input().split()]
cb,b = [int(e) for e in input().split()]
w = cb-b
if w >= a:
	b = b+a
	a = 0	
else :
	a = a-w
	b = cb
print(a,b)