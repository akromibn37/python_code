n = int(input())
fruit = []
for i in range(n):
    l = input().strip().split()
    for j in range(1,len(l)):
        l[j] = float(l[j])
    fruit.append(l)

c = input().split() # อ่ำนคำสั่งที่ต้องกำรประมวลผล
if c[0] == 'show' :
    for f in fruit:
        print(' '.join([str(e) for e in f]))
        
elif c[0] == 'max' :
    m = 0
    k = int(c[1])
    for i in range(1,n):
        if fruit[i][k] > fruit[m][k]:
            m = i
        elif fruit[i][k] == fruit[m][k] and fruit[i][0] < fruit[m][0]:
            m = i
    print(fruit[m][0],fruit[m][k])

elif c[0] == 'avg' :
    k = int(c[1])
    avg = sum([f[k] for f in fruit])/n
    print( round( avg , 4) )

elif c[0] == 'get' :
    x = c[1]
    for f in fruit:
        if f[0]==x:
            print(' '.join([str(e) for e in f]))
            break
    else:
        print(x,'not found')

elif c[0] == 'sort' :
    k = int(c[1])
    L = [[f[k],f[0]] for f in fruit]
    L.sort()
    print(' '.join([x[1] for x in L]))
