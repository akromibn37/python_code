a = input().strip()
b = input().strip()
a = a[1:len(a)-1]
b = b[1:len(b)-1]
a = a.split(",")
b = b.split(",")
sum = 0
for i in range(len(a)):
	sum += int(a[i])*int(b[i])
print(sum)
