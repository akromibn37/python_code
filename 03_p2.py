import math
n,r,m = [int(e) for e in input().split()]
nf = math.factorial(n)
rf = math.factorial(r)
nrf = math.factorial(n-r)
if m == 1:
	result = nf/nrf
else:
	result = nf/(nrf*rf)
print(int(result))