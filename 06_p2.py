n = int(input().strip())
i = 0
l =[]
sum = 0
while i<n:
	l.append(int(input().strip()))
	i+=1
data = [int(e) for e in input().split()] 
for i in range(data[0],data[1]+1):
	sum+=l[i]
print(sum)