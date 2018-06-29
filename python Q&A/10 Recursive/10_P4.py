def PowerMod(a, k, m) :
    if k == 0 : return 1
    if k%2 == 0 :
        return PowerMod(a, k//2, m) ** 2 % m
    else :
        return a*PowerMod(a, k//2, m) ** 2 % m

a, k, m = [int(x) for x in input().split()]
print(PowerMod(a, k, m))


