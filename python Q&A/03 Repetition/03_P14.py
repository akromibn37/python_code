a,b = [int(e) for e in input().split()]
if b == 1:
    for i in range(1,a+1):
        for j in range(i,a+1):
            print('('+str(i)+','+str(j)+')')
elif b == 2:
    for i in range(1,a+1):
        for j in range(1,i+1):
            print('('+str(i)+','+str(j)+')')
elif b == 3:
    for i in range(1,a+1):
        print('('+str(i)+','+str(a-i+1)+')')
