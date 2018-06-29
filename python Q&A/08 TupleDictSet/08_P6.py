n,m = [int(e) for e in input().split()]
d = [int(e) for e in input().split()]
q = [int(e) for e in input().split()]
sum = { d[a]+d[b] for a in range(n) for b in range(a+1,n) }
p = { s:[] for s in sum }
for a in range(n):
    for b in range(a+1,n):
        p[d[a]+d[b]].append((a,b))

for i in range(m):
    for j in range(n):
        x = q[i] - d[j]
        if x in p:
            for (a,b) in p[x]:
                if j!=a and j!=b:
                    print("YES")
                    break
            else:
                continue
            break
    else:
        print("NO")
