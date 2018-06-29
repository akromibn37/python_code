w = input().strip()
x = ""
if w.find(" ")!=-1:
	for i in w:
		if i!=" ":
			x+=i.lower()
else:
	x = w.lower()

x1 = ""
for i in range(len(x)-1,-1,-1):
	x1+=x[i]

if x==x1:
	print("yes")
else:
	print("no")