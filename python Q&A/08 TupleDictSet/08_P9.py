n = int(input())
d = [int(input()) for i in range(n)]
counts = {}
for e in d:
    if e not in counts: counts[e] = 0
    counts[e]+=1
maxcount, maxnum = min([(-counts[c],c) for c in counts])
print(maxnum)
