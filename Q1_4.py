n,a = [int(e) for e in input().split()]
c = 0
out = ""
t = n
i = 1
while t > 0:
	x = t%10
	t = t//10
	x = c+x
	if i<=a:
		if x>5:
			c = 1
			out = "0" + out
		elif x<5:
			c = 0
			out = "0" + out
		else:
			if (t%10)%2==0:
				c = 0
				out = "0" + out
			else:
				c =1
				out = "0" + out
	else:
		out = str(x) + out
		c = 0
	i+=1
print(out)
		