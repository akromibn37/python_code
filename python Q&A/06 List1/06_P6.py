a = [int(e) for e in input().split()]
if len(a) == 1:
    b = a
else:
    b = []
    if len(a) > 2 :
        for i in range(1,len(a)-1):
            b.append((a[i-1]+a[i]+a[i+1])//3)
    b.insert(0,(a[0]+a[1])//2)
    b.append((a[-2]+a[-1])//2)
b = [str(e) for e in b]
print(' '.join(b))
