data = input().strip()
l = data.split(",")
sum = 0
for i in range(len(l)):
	if i>0:
		if int(l[i]) <0:
			if int(l[i-1]) < 0 :
				sum = sum
			else:
				sum +=1
	else :
		if int(l[i])>0:
			sum+=1
print(sum)
		
