r,c = [int(e) for e in input().split()]
l1 = [[0 for x in range(c)] for y in range(r)] 
l2 = [[0 for x in range(c)] for y in range(r)] 
for i in range(2):
	for j in range(r):
		if i==0:
			l1[j] = [int(e) for e in input().split()]
		else:
			l2[j] = [int(e) for e in input().split()]
l3 = [[0 for x in range(c)] for y in range(r)] 
for i in range(r):
	for j in range(c):
		l3[i][j] = l1[i][j]+l2[i][j]
	print(' '.join([str(e) for e in l3[i]]))
		