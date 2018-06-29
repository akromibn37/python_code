file = input().strip()
f = open(file)
fruit = []
ans = []
max = 0 
maxnum = 0
for line in f:
	line = line.strip()
	if line == '': continue
	fr,na = line.split(" ")
	if fr not in fruit:
		t = []
		l = []
		fruit.append(fr)
		l.append(na)
		t.append(fr)
		t.append(l)
		ans.append(t)
	else:
		k = fruit.index(fr)
		x = ans[k]
		x = x[1]
		l = []
		x.append(na)
		l.append(fr)
		l.append(x)
		ans.pop(k)
		ans.insert(k,l)
for i in range(len(ans)):
	y = ans[i]
	y = y[1]
	if len(y)>max:
		max = len(y)
		nummax = i
print(ans)
print("The most favorite fruit is " + ans[nummax][0])
	
	
		