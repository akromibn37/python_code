f = open("score.txt")
l = []
for line in f:
	x = line.split()
	l.append(x)
f.close()
#print(l)
l.sort(reverse=True)
for i in l:
	print(i[0])