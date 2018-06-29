import math
n = int(input())
result = 0
i = 0
while n>0:
	k = n%10
	r = math.pow(2,i)
	result += k*r
	n = n//10
	i+=1
print(int(result))