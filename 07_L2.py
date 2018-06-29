s = input().strip()
x = [int(e) for e in s.split()]
k = 0
#for k in range(len(x)-1):
while k<len(x)-1:
	minIdx = k
	minVal = x[k]
	i = k
	#for i in range(len(x)):
	while i<len(x):
		if x[i]< minVal:
			minIdx = i
			minVal = x[i]
		i+=1
	x[k],x[minIdx] = x[minIdx],x[k]
	k+=1
print(x)
