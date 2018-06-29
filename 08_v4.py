c = dict()
while True:
	x = input().split()
	if x[0] == '-1':break
	for e in x[1:]:
		if e not in c:
			c[e] = set()
		c[e].add(x[0])
#print(c)
c1,c2 = input().split()
if c1 in c:
	cc1 = c[c1]
else:
	cc1 = set()
if c2 in c:
	cc2 = c[c2]
else:
	cc2 = set() 
i = len(cc1&cc2)
j = len(cc1|cc2)
print(i,(j-i),j)