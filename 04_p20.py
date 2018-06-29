c = input().strip()
x = 0
y = 0
for i in c:
	if i == "U":
		y+=1
	elif i == "R":
		x+=1
	elif i == "D" and y>0:
		y-=1
	elif i=="L" and x>0:
		x-=1
print("(" + str(x)+","+str(y) + ")")