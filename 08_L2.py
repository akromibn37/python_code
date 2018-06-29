f = open("address.txt")
d = dict()
for line in f:
	l = line.split()
	n = l[0]+" " +l[1]
	t = l[2]
	d[n]=t
#print(d)
f.close()
o = input().strip()
while True:
	if o == "": break
	if o.isnumeric():		
		for k,i in d.items():
			if i == o:
				print(k)
				break
		print("Not Found")
	else:
		tel = d.get(o,"Not Found")
		print(tel)
	o = input().strip()
