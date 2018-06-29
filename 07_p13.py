r = int(input())
c = int(input())
l = [[0 for x in range(c)] for y in range(r)] 
b = False
for i in range(r):
	l[i] = [e for e in input().split()]
for i in range(r):
	if b == True:
		break
	for j in range(i+1,r):
		if l[i]==l[j]:
			print(i+1)
			print(' '.join([str(e) for e in l[i]]))
			print(j+1)
			print(' '.join([str(e) for e in l[j]]))
			b = True
			break
			