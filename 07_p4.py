c = input().strip()
num = []
count = []
n = 0
while c!='-1':
	if c in num:
		count[num.index(c)]+=1
	else :
		num.append(c)
		count.append(1)
	c = input().strip()
	n+=1
f = n//2
#print(f)
#print(num)
#print(count)
found = False
for i in range(len(count)):
	if count[i]>f:
		print(num[i])
		found = True
if found == False:
	print("Not found")