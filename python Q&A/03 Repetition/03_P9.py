a,b,c,xn,d = [float(e) for e in input().split()]
n = 1
while True:
    xn1 = xn - (a*xn**2+b*xn+c)/(2*a*xn+b)
    if (abs(xn1-xn) <= d) : break
    xn = xn1
    n += 1
print(n)
