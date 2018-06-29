l = []
c = input().strip()
while c != 'end':
	if c == 'list':
		print(l)
	elif c == 'shelf':
		if len(l)>0:
			x=l.pop(len(l)-1)
			print(x)
		else:
			print("no book")
	elif c == 'top':
		if len(l)>0: 
			print(l[len(l)-1])
		else:
			print("no book")
	else:
		l.append(c[7:])
		print(len(l))
	c = input().strip()
	