filename = input().strip()
a = input().strip()
na = 0
b = input().strip()
nb = 0
c = input().strip()
nc = 0
f = open(filename,'r')
for line in f:
	if a in line:
		na += line.count(a)
	if b in line:
		nb += line.count(b)
	if c in line:
		nc += line.count(c)
f.close()
if na > nb > nc : print(a+b+c)
if na > nc > nb : print(a+c+b)
if nb > na > nc : print(b+a+c)
if nb > nc > na : print(b+c+a)
if nc > na > nb : print(c+a+b)
if nc > nb > na : print(c+b+a)
	
		
