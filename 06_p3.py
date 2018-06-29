n = int(input().strip())
data = [int(e) for e in input().split()] 
sum = 0
for i in range(len(data)):
	sum += data[i]
print(sum/n)