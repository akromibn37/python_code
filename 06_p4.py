data = [int(e) for e in input().split()] 
sum = 0
for i in range(len(data)-1):
	sum += data[i]
print(sum/(len(data)-1))