a = input().strip().lower()
i = 0 
current = 0
longest = 0
while i != len(a)-1:
	c = a[i]
	print(c)
	current +=1
	print("current",current)
	if a[i+1] == c :
		i+=1
		print(i)
	else:
		if current > longest :
			longest = current
			print("longest", longest)
		current = 0
		i+=1
		print(i)
	if i == len(a)-1 :
		if c == a[i] : current+=1
		if current > longest :
			longest = current
			print("longest", longest)
if len(a) == 1:
	longest = 1
print(longest)