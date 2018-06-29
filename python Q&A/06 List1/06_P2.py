n = int(input())
d = []
for i in range(n):
    x = int(input())
    d.append(x)
a,b = [int(e) for e in input().split()]
print(sum(d[a:b+1]))
