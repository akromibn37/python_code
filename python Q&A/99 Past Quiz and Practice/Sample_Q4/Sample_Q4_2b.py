def F(n):
    if n == 0 : return 0
    if n == 1 or n == 2 : return 1
    m = n//3
    fm = F(m)
    if n%3 == 0:
        return 5*fm**3 + 3*(-1)**m*fm
    f = F(m+1)
    if n%3 == 1:
        return f**3 + 3*f*fm*fm - fm**3
    return f**3 + 3*f*f*fm + fm**3

def x(m,n):
    if n == 0 : return m
    if m == 0 : return n
    return x(m,n-1)+x(m-1,n)

def p(n):
    if n <= 1 : return n
    if n%2 == 0 :
        return n + 2*p(n-1) + p(n-2)
    return n + p(n-1) + 2*p(n-2)

def z1(n):
    if n < 10 : return z2(n)
    x = z2(n)
    return z1(x) + x

def z2(n):
    if n < 10 : return n
    return n%10 + z2(n//10)

exec(input().strip())
