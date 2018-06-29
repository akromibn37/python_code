w = input()
out = True
for i in range(len(w)-1):
	a = w[i].lower()
	b = w[i+1].lower()
	if a>b :
		out = False
		break
if out==True:
	print("yes")
else:
	print("no")
	