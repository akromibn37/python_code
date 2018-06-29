n = int(input())
d = [input().strip() for e in range(n)]
for k in range(n-1):
    for i in range(n-1):
        for c in 'abcdefghijklmnopqrstuvwxyz' :
            c1 = d[i].count(c)
            c2 = d[i+1].count(c)
            if c1 < c2:
                break
            elif c1 > c2:
                d[i],d[i+1] = d[i+1],d[i]
                break
        else:
            if d[i] > d[i+1]:
                d[i],d[i+1] = d[i+1],d[i]
print('\n'.join(d))
