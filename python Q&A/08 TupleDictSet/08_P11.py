from collections import defaultdict

n = int(input())
act = dict()
for k in range(n):
    s = set(input().split())
    for a in s:
        if a not in act: act[a] = defaultdict(int)
        for b in s:
            if a != b:
                act[a][b] += 1
x = input().strip()
if x not in act :
    print('Not Found')
else:
    if len(act[x]) == 0 :
        print('No suggested event')
    else:
        w = [(-act[x][a],a) for a in act[x]]
        w.sort()
        print(w[0][1])
        print(-w[0][0])
