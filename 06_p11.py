data = [int(e) for e in input().split()]
sum1 = 0
sum2 = 0
i = 1
while len(data)>0:
	x = len(data)-1
	if data[0] > data[x]:
		if i %2 == 0:
			sum2 += int(data.pop(0))
		else:
			sum1 += int(data.pop(0))
	else:
		if i %2 == 0:
			sum2 += int(data.pop(x))
		else:
			sum1 += int(data.pop(x))
	i+=1
print(sum1)
print(sum2)
if sum1>sum2:
	print("1")
elif sum1==sum2:
	print("0")
else:
	print("2")