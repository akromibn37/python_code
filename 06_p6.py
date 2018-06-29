data = [int(e) for e in input().split()]
ans = ""
for i in range(len(data)):
	mov = data[i]
	if len(data)>1:
		if i == 0:
			mov = (data[i]+data[i+1])//2
		elif i==len(data)-1:
			mov = (data[i]+data[i-1])//2
		else:
			mov = (data[i]+data[i-1]+data[i+1])//3
	ans+= str(mov) + " "
print(ans)