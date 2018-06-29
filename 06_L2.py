x = input().strip()
a = x.split(" ")
b = []
no = 0
print(a)
if a != ['']:
	for i in range(len(a)):
		e = a[i]
		if int(e)%2==1:
			b.append(1)
			no+=1
		else:
			b.append(0)
print(b)
print(no)