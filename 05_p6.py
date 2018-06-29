f1 = input().strip()
f2 = input().strip()
fn1 = open(f1,'r')
fn2 = open(f2,'r')
k = 0
for line in fn1:
	i = int(line.strip())
	sum = 0 
	for x in range(i):
		j = float(fn2.readline().strip())
		sum += j
		k+=1
	print(sum/i)
			