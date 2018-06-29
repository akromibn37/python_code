n = int(input().strip())
d = dict()
for i in range(n):
	line = input().strip()
	l = line.split(":")
	x = l[1].split(",")	
	d[l[0]]=x
	#print(d)

f = input().strip()
k = d[f]
t = set()
check = False
for i in range(len(k)):
	for x in d.keys():
		if (k[i] in d[x]) and (x!=f) and (x not in t):
			t.add(x)
			print(x)
			check=True
if check == False:
	print("Not Found")
		
	