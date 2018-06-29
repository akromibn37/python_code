c,n = [int(e) for e in input().split()]
l = [[0 for x in range(n)] for y in range(c)] 
for i in range(c):
	l[i] = [e for e in input().split()]
	#print(l[i])
for i in range(c):
	s = 0
	x = 0
	for j in range(n):
		#print(l[i][j])
		if l[i][j] == 'A':
			s+=4.0
		elif l[i][j] == 'B+':
			s+=3.5
		elif l[i][j] == 'B':
			s+=3.0
		elif l[i][j] == 'C+':
			s+=2.5
		elif l[i][j] == 'C':
			s+=2.0
		elif l[i][j] == 'D+':
			s+=1.5
		elif l[i][j] == 'D':
			s+=1.0
		elif l[i][j] == 'X':
			s+=0
			x+=1
		elif l[i][j] == 'F':
			s+=0
	s = s/(n-x)
	print("{:.2f}".format(s))
