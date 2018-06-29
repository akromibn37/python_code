w = input().strip()
c = input().strip()
c1 = input().strip()
out = ""
for i in w:
	if i == c1:
		out += c
	elif i == c:
		out+=c1
	else:
		out+=i
print(out)