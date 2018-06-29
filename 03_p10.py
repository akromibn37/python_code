n = int(input())
out = ""
for i in range(n-1,1,-1):	
	if n%i==0:
		out+= str(i)+ " "
if out == "":
	print("Prime Number")
else:
	print(out)