f = open("score.txt",'r')
i = int(input())
found = False
for line in f :
	sid,g = line.strip().split(" ")
	if int(sid) == i :
		print(g)
		found = True
		break
if	found == False :
	print("Not Found")