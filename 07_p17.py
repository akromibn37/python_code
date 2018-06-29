l = []
num = ''
b=False
while True:
	c = [e for e in input().split()]
	if len(c)==1:
		num = c
		break
	else:
		c[1] = float(c[1])
		c[0],c[1] = c[1],c[0]
		l.append(c)
#print(l)
l.sort()
#print(l)
#print(num)
for i in range(len(l)):
	#print(num[0],l[len(l)-1-i][1])
	if num[0] == l[len(l)-1-i][1]:
		print(i+1)
		b = True
		break
if b == False:
	print("Not Found")
