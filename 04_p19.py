w1 = input().strip()
w2 = input().strip()
x = ""
for i in w1:
	for j in w2:
		if j == i:
			if j not in x:
				x+=j
x = sorted(x,key=str.swapcase)
out = ""
for i in x:
	out += i + " "
if out == "":
	print("NONE")
else:
	print(out)


	