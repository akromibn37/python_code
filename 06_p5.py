data = [int(e) for e in input().split()] 
dat = []
dat.append(data)
while data[0] != -1:
	data = [int(e) for e in input().split()]
	dat.append(data)
for i in range(len(dat)-1):
	bmi = dat[i][0]/((dat[i][1]/100)**2)
	print(bmi)