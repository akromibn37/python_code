r,c = [int(e) for e in input().split()]
out = ""
for i in range(1,r+1):
	for j in range(1,c+1):
		out += str(i*j) + " "
	print(out)
	out = ""
	