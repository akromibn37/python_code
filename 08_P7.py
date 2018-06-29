n = int(input().strip())
i = 0
d = dict()
while i<n:
	w = input().split()
	print(w)
	w2 = w[1][:2]
	if w2 not in d:d[w2] = []
	d[w2].append(w[1])
	i+=1
nmax,w2max = min([(-len(d[w2]),w2) for w2 in d])
print(w2max)
print(-nmax)
print('\n'.join(d[w]))
	