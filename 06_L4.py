data = [int(e) for e in input().split()] 
r = len(data)+1
dat = []
dat.append(data)
ans = 0
i = 0
while i<(r/2-1):
	data = [int(e) for e in input().split()] 
	dat.append(data)
	i+=1
for i in range(int(r/2)):
	for j in range(r-1):
		if ((r/2-1)-i) <= j <= ((r/2-1)+i):
			print(i,j)
			ans += dat[i][j]
print(ans)