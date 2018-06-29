n = int(input())
p = False
for x in range(n):
	for y in range(x,n):
		if x**2 + y**2 == n:
			print(x,y)
			p = True
if p==False:
	print("No solution")