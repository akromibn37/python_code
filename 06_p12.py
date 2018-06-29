data = input().strip()
l = []
for x in range(len(data)):
	l.append(data[x])
num = int(input().strip())
out = ""
i = 0
while i<num:
	out = ""
	command = [e for e in input().split()]
	if command[0] == "in":
		l.insert(int(command[2]),command[1])
	elif command[0] == "out":
		l.pop(int(command[1]))
	elif command[0] == "swap":
		x = l[int(command[1])]
		y = l[int(command[2])]
		l[int(command[1])] = y
		l[int(command[2])] = x
	for j in range(len(l)):
		out += l[j]
	print(out)	

	i+=1
	
	