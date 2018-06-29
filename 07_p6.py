n = int(input())
i = 0
l = []
m = []
mn = []
while i<n:
	s = int(input())
	if s not in m:
		m.append(s)
		mn.append(1)
	else:
		mn[m.index(s)]+=1
	l.append(s)
	i+=1
#print(l)
l.sort()
#print(l)
mean = sum(l)/n
if n%2!=0:
	med = l[int((n+1)/2-1)]
else:
	x1 = int(n/2-1)
	x2 = int((n/2))
	med = (l[x1] + l[x2])/2
mode = m[mn.index(max(mn))]
print(mean,med,mode)	


