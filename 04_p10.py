w = input().strip()
x = input().strip()
x1 = input().strip()
out = ""
for i in w:
	k = 0
	for j in range(len(x)):
		if i == x[j]:
			out+=x1[j]
			k+=1
		elif i==x1[j]:
			out+=x[j]
			k+=1
	if k==0:
		out+=i
print(out)