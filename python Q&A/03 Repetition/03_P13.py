a,b = [int(e) for e in input().split()]
for i in range(1,a+1):
    out = ''
    for j in range(1,b+1):
        out += str(i*j) + ' '
    print(out)
