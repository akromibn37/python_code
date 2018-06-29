d = [int(e) for e in input().split()]
n = len(d)
for k in range(n-1):
    for i in range(n-1):
        if d[i] > d[i+1]:
            d[i],d[i+1] = d[i+1],d[i]
print((d[n//2]+d[(n-1)//2])/2)
