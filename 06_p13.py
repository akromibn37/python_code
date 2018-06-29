n = int(input().strip())
i = 0
x = []
out = "1 "
while i<n:
	x.append(int(input().strip()))	
	i+=1
i = 1
while i<n:
	if i==1:
		c = x[0]
		out += str(c) + " "
	else:
		c = x[c-1]
		out += str(c) + " "
	i+=1
print(out)
	
