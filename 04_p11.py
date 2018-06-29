w = input().strip()
a,b = [int(e) for e in input().split()]
w0 = w[:a]
w1 = w[b+1:]
w2 = w[a:b+1]
c = ""
for i in range(len(w2),0,-1):
	c+= w2[i-1]

print(w0+c+w1)