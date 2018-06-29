m,n = [int(e) for e in input().split()]
l = [[0 for x in range(n)] for y in range(n)] 
for i in range(n):
	l[i] = [e for e in input().split()]
	#print(l[i])
if m == 0:
	s = 0
	for i in range(n):
		for j in range(n):
			if j<=i:
				s+=int(l[i][j])
			else: continue
	print(s)
else:
	s = 0
	for i in range(n):
		for j in range(n):
			if j>=i:
				s+=int(l[i][j])
			else: continue
	print(s)

