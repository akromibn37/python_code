filename = input().strip()
f = open(filename)
l = []
for line in f:
	lx = line.split(";")
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
	l.append(lx)

print(l)