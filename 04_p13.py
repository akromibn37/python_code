w = input().strip()
s = 0
c = 0
for i in w:
	if i.lower() in "aeiou":
		c+=1
	else:
		if c>0:
			s+=1
			c=0

if c>0:
	s+=1
print(s)