n = int(input())
w = 2*n +1
if n%2==0:
	h = (2*n)-1
else:
	h = (2*n)-2
h1 = n//2
h2 = h1+(n//2)-2
h3 = n+1
for i in range(n//2):
    dot = (n//2-1-i)
    sharp = n-2*dot
    pic = '.'*dot + '#'*sharp + '.'*dot
    print(pic+'.'+pic)
for i in range(n//2-2):
    print('#'*(2*n+1))
hx = 1
for i in range(1,h3+1):
	outx = ""	
	for j in range(1,w+1):
		if j>=hx and j<(w+2-i):
			outx += "#"
		else:
			outx += "."
	hx +=1
	print(outx)





				
				
				
