infile = open("inventory.txt", "r")
inven = []
for line in infile:
	[code, name, amount] = line.split(";")
	inven.append([code, name, int(amount)])
infile.close()
c = input().strip()
while c!= 'Q':
	l = c.split()
	if l[0] == 'T':
		found = False
		for i in range(len(inven)):
			if inven[i][0] == l[1]:
				inven[i][2] += int(l[2])
				print(inven[i])
				found = True
				break;
		if found == False:
			print("Product code does not exist.")
	elif l[0] == 'U':
		found = False
		for i in range(len(inven)):
			if inven[i][0] == l[1]:
				inven[i][2] = int(l[2])
				print(inven[i])
				found = True
				break;
		if found == False:
			print("Product code does not exist.")
	elif l[0] == 'A':
		found = False
		for i in range(len(inven)):
			if inven[i][0] == l[1]:
				print("Duplicate product code.")
				found = True
				break;
		if found == False:
			inven.append([l[1], l[2], int(l[3])])
			print(inven[len(inven)-1])
	elif l[0] == 'D':
		found = False
		for i in range(len(inven)):
			if inven[i][0] == l[1]:
				found = True
				inven.pop(i)
				print(l[1],"deleted")
				break;
		if found == False:
			print("Product code does exist.")
	c = input().strip()
if c == 'Q':
	print("Bye!")
	