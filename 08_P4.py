c = [int(e) for e in input().split()]
s = int(input().strip())
count = 0
for i in range(len(c)-1):
	for j in range(i+1,len(c)):
		if c[i]+c[j] == s:
			count+=1
print(count)
