n = [int(e.strip()) for e in input().split()]
t=set(n)
check = False
for i in range(len(t)):
	if n.count(list(t)[i])==1:
		print(list(t)[i])
		check = True
		break
if check == False:
	print("NONE")