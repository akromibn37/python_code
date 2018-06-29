n,r,mode = [int(e) for e in input().split()]
t = 1
for x in range(n-r+1, n+1):
    t *= x
if mode == 1:
    print(t)
elif mode == 2:
    for x in range(1,r+1):
        t //= x
    print(t)
