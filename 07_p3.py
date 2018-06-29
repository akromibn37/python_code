f = open("score.txt")
li = []
g = []
for i in f:
	j = i.split()
	li.append(j[0])
	g.append(int(j[1]))
f.close()
c = input().strip()
while c!='-1':
	if c in li:
		k = li.index(c)
		print(g[k])
	else:
		print("Not Found")
	c = input().strip()