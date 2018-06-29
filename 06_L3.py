data = [int(e) for e in input().split()] 
print(data)
diff1 = data[1]-data[0]
diff2 = data[2]-data[1]
if diff1 == diff2:
	print(data[-1])
	print(data[-1]+diff1)
else:
	diff1 = data[2]-data[0]
	diff2 = data[3]-data[1]
	print(diff1,diff2)
	print(data[-2])
	if len(data)%2==0:
		print(data[-2]+diff1)
	else:
		print(data[-2]+diff2)