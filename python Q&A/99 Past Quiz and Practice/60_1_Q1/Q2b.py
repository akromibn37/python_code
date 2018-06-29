c = input().strip()

if c=='Y':
    n = int(input())
    p = 1
    r = 0
    t = 1
    k = 1
    m = 3
    z = 3
    i = 1
    q = ''
    while i < n:
        if 4*p+r-t < m*t:
            q = q+str(m)
            b = 10*(r-m*t)
            m = 10*(3*p+r)//t-10*m
            p = 10*p
            r = b
        else:
            b = (2*p+r)*z
            a = (7*p*k+2+z*r)//(z*t)
            p = k*p
            t = z*t
            z = z+2
            k = k+1
            m = a
            r = b
        i += 1
    q = q[0]+'.'+q[1:]
    print('pi =', q)

elif c=='X':
    n = int(input())
    q = 0
    for k in range(n+1):
        q += (-1)**(-k)/(2*k+1)
    q = 4*q
    q = round(q,7)
    print('pi =', q)

elif c=='Z':
    q = (2**4+3**4+1/(2+1/4))**0.25
    q = round(q,7)
    print('pi =', q)

else:
    print('Invalid')
