n = int(input())
l = [[0 for x in range(n)] for y in range(n)] 
b = False
for i in range(n):
	l[i] = [e for e in input().split()]
	#print(l[i])
for i in range(n):
	if l[i].count('1')==1:
		print(l[i].index('1'))
		b = True
		break
if b == False:
	print("-1")