import math
n = float(input().strip())
s = 0.0
t = n
x = 0
if n<0:
	print("ERROR")
else:
	if n>80:
		x = math.ceil(t-80)
		t = t-x
		s += 10.5*x		
	if n>=60:
		x = math.ceil(t-60)
		t = t-x
		s+=9*x	
	if n>=40:
		x = math.ceil(t-40)
		t = t-x
		s+=8*x
	if n>=20:
		x = math.ceil(t-20)
		t = t-x
		s+=7.5*x
	if n>=10:
		x = math.ceil(t-10)
		t = t-x
		s+=6.5*x
	if n>=1:
		x = math.ceil(t-1)
		t = t-x
		s+=5.5*x
	if n>0:
		s+=35
	print(s)

	