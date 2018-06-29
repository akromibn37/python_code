n = int(input())
result = 0
for i in range(1,n+1):
	for j in range(1,i+1):
		for k in range(1,j+1):
			result += (-1)**i*j*k
print(result)