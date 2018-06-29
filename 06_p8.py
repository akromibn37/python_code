n = int(input().strip())
l = []
for i in range(n):
	l.append(i+1)
data = [int(e) for e in input().split()]
while data[0]!=0 and data[1]!=0:
	x = l.index(data[0])
	y = l.index(data[1])
	l[x] = data[1]
	l[y] = data[0]
	data = [int(e) for e in input().split()]	
print(l)
