a = int(input().strip())
l = []
l.append(a)
while a>=0:
	a = int(input().strip())
	l.append(a)
x = l.pop()
while len(l)>0:
	print(l.pop(0)+x)