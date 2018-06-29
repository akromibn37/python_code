import math
n,b = [int(e) for e in input().split()]
out = ""
if b >=2 and b<=9 and n>=0:
	if n==0:
		out="0"	
	while n>0:
		out = str(n%b) + out
		n //=b		
	
	print(out)
else:
	print("Error: Cannot convert")