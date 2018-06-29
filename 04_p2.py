word = input()
sv = 0
sc = 0
for i in word:
	c = i.lower()
	if c in "aeiou":
		sv+=1
	elif "a" <= c <= "z":
		sc+=1
print(sv,sc)
