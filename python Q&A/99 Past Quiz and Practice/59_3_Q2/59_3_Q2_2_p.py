op = input().strip()

if op == 'A':
    m = int(input())
    p = int(input())
    q = int(input())
    for i in range(m+1):
        for j in range(p):
            if i+j > q:
                print('P3',i,j)
                break
        else:
            print('P4',i,j)

elif op == 'B':
    m = int(input())
    p = int(input())
    i = c = 0
    while i <= m:
        j = i
        while j <= p:
            print(i,j)
            c += 1
            j += 1
        i += 1
    print(c)

else:
    print('Invalid op')
