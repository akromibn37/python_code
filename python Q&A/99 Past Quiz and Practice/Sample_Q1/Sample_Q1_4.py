n,d = [int(e) for e in input().split()]
k = n%10**d
c = n - k
if k//10**(d-1)< 5:
    print(c)
elif k//10**(d-1)>5:
    print(c+10**d)
else:
    if c//10**d%2 == 0:
        print(c)
    else:
        print(c+10**d)
