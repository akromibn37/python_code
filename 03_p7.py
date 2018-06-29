n,m = [int(e) for e in input().split()]
s = 0
for i in range(n):
	n1 = int(input())
	if n1==m:
		s+=1
print(s)