n = int(input().strip())
i =0
x = []
while i<n:
	x.append(int(input()))
	i+=1
for j in range(n-1):
	for k in range(j+1,n):
		if x[j]<=x[k]: 
			x[j],x[k]=x[k],x[j]
for j in range(n):
	print(x[j])