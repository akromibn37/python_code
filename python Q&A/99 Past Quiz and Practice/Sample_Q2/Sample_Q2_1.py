m = int(input())
c = 0
np = 0
while c < m :
    n = int(input())
    t = 0
    d = 1
    while d <= n//2:
        k = n%d
        if k == 0:
            t = t+d
        d += 1
    if t == n:
        s = str(n) + ' is perfect'
        print(s)
        np += 1
        t = 0
        d = 1
        s = ''
        while d <= n//2:
            k = n%d
            if k == 0:
                t = t + d
                s += str(d) + ','
            d += 1
        print(s)
    else:
        s = str(n) + ' is not perfect'
        print(s)
    c += 1
print(np)
