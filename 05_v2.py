'''infile = open("data.txt",'r')
for line in infile :
	print(line)'''

n = int(input())
i = 1
found = False
infile = open("data.txt",'r')
for line in infile:	
	if "Name:" in line :
		if i==n :
			print(line[6:])
			found = True
		i+=1
infile.close()

if found == False:
	print("Not found")
		