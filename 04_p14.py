n = input().strip()
s=0
x1=0
x2=0
if n[0] in "+-":
	a = 0
else :
	a = ""
for i in n:
	if i in "+-":
		x1 = int(a)
		s+=x1
		a = ""
		a+=i
	else :
		a+=i
s+=int(a)
print(s)