a = input().strip()
a = a[1:-1].split(",")
a = [int(e) for e in a]
b = input().strip()
b = b[1:-1].split(",")
b = [int(e) for e in b]
dot = sum([a[i]*b[i] for i in range(len(a))])
print(dot)
