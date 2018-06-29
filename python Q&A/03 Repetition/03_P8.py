n = int(input())
maxC = 1
for a in range(1,n-2):
    for b in range(a,n-a):
        c = n - (a+b)
        if c**2 == a**2+b**2:
            if c > maxC:
                maxC = c
print(maxC)
