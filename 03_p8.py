c = int(input())
m = 0
x = 0
for i in range(1,c-2):
	for j in range(i,c-i):
		if i**2 + j**2 == (c-(i+j))**2:
			x = c-(i+j)			
		if x>m:
			m=x
print(m)
	