n = int(input())
if n <= 100000:
    print(0.05*n)
elif n <= 500000:
    print(5000+0.1*(n-100000))
elif n <= 1000000:
    print(45000+0.2*(n-500000))
elif n <= 4000000:
    print(145000+0.3*(n-1000000))
else:
    print(1045000+0.37*(n-4000000))
