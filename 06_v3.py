filename = input().strip()
f = open(filename)
l = []
sid = []
for line in f:
	line = line.strip()
	if line == '' : continue	
	else:
		lx = line.split(";")
		if lx[0] not in sid:
			s1 = lx.pop()
			s2 = lx.pop()
			n = lx.pop()
			n = lx.pop() + " "+ n
			lx.append(n)
			score = float(s1)+float(s2)
			if score >= 80:
				score = 'A'
			elif score >=70:
				score = 'B'
			elif score >=60:
				score = 'C'
			elif score >= 50:
				score = 'D'
			elif score >= 0:
				score = 'F'
			lx.append(score)
			sid.append(lx[0])
			l.append(lx)
f.close()			
i = input().strip()
while i!= '-1':
	if i not in sid:
		print("Not Found")
	else:
		k = sid.index(i)
		print(l[k])
	i = input().strip()