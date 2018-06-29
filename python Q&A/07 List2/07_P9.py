a = [int(e) for e in input().split()]
x = [e for e in a if e%2 == 0]
y = [e for e in a if e%2 == 1]
w = sorted(x) + sorted(y)[-1::-1]
z = [str(e) for e in w]
print(" ".join(z))
