r,c = [int(e) for e in input().split()]
l = [[0 for x in range(c)] for y in range(r)] 
b = False
for i in range(r):
	l[i] = [e for e in input().split()]
	#print(l[i])
for i in range(r):
	minnum = min(l[i])
	minindex = l[i].index(minnum)
	#print(minnum,minindex)
	if b == True:
		break
	for j in range(r):
		if j!=i and minnum<l[j][minindex]:
			break
		elif j == r-1:
			print(minnum)
			b = True
			break
if b == False:
	print("-1")