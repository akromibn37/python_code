b = input().strip()
s = 0
for i in b:
	if i == "1":
		s+=1
if s%2==0:
	print(b+"0")
else:
	print(b+"1")
	
	