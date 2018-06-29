filename = input().strip()
f = open(filename,'r')
l = f.readline().strip()
for line in f:
	sid,q1,q2,q3,q4,q5 = line.strip().split(" ")
	sum = int(q1)+ int(q2)+ int(q3)+ int(q4)+ int(q5)
	if sum >=80 :
		sid += " A"
	elif sum >= 75 :
		sid += " B+"
	elif sum >= 70 :
		sid += " B"
	elif sum >= 65 :
		sid += " C+"
	elif sum >= 60 :
		sid += " C"
	elif sum >= 55 :
		sid += " D+"
	elif sum >= 50 :
		sid += " D"
	elif sum < 50 :
		sid += " F"
	print(sid)
f.close()