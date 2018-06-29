import math
x = float(input())
cos = (math.pow(-1,0)*math.pow(x,0))/math.factorial(0)
sum = cos
k = 0
while abs(cos)>math.pow(10,-8) :
	k+=1
	cos = (math.pow(-1,k)*math.pow(x,2*k))/math.factorial(2*k)
	sum+=cos
	
print(sum,k-1)