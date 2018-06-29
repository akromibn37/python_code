i = int(input())
t = ""
eo = ""
if i%2==0:
	eo = "even"
else :
	eo = "odd"
if i<0:
	t = "negative"
if i == 0:
	t = "zero"
if i>0:
	t = "positive"
print(t,eo)