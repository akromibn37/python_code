n = int(input())
c = []
for k in range(n):
    c.append(input().split())
for i in range(n):
    cr = 0
    for j in range(n):
        if c[i][j] == '1' :
            cr += 1
    if cr != 1 : continue
    cc = 0
    for j in range(n):
        if c[j][i] == '1' :
            cc += 1
    if cc == n :
        print(i)
        break
else:
    print(-1)
