data = [e for e in input().split()]
pos = [int(e) for e in input().split()]
out = ""
for i in range(len(data)):
	out += data[pos[i]] + " "
print(out)