n,t = [int(e) for e in input().split()]
if t !=3:
	for i in range(1,n+1):
		for j in range(1,n+1):
			if t == 1:
				if j>=i:
					print("(" + str(i)+","+str(j) + ")")
			elif t==2:
				if i>=j:
					print("(" + str(i)+","+str(j) + ")")
else:
	for i in range(1,n+1):
		print("(" + str(i)+","+str(n-i+1) + ")")

			