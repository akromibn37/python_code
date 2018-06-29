n = int(input())
out = ""
for i in range(1,n+1):
	check = 0
	for j in range(1,i+1):
		if i%j==0:
			check+=1
	if check ==2:
		out += str(i) + " "

if out == "":
	if n<0:
		print("input unavailable")
	else:
		print("none")
else:
	print(out)