f=open("books.txt")
d=dict()
for line in f:
	k = line.strip().split(",")
	for i in range(1,len(k)):
		k[i] = k[i][1:]
	d[k[0]] = list(k[1:])
#print(d)
a = input().strip().split(",")
for i in range(1,len(a)):
		a[i] = a[i][1:]
check2 = False
for k in d.keys(): 
	check = True
	for i in range(len(a)):
		#print(i,a[i])
		if a[i] not in d[k]:
			check = False
			break
	if check == True:
		print(k)
		check2 = True
if check2 == False:
	print("Not Found")