import math

a = float(input())
n = int(input())
if 3 <= n <= 7 :
    if n == 3 :
        ar = 3**0.5/4*a**2
    elif n == 4:
        ar = a**2
    elif n == 5:
        ar = 1/4*(5*(5+2*5**0.5))**0.5*a**2
    elif n == 6:
        ar = 3*3**0.5/2*a**2
    else :
        ar = 7/4*a**2/math.tan(math.radians(180/7))
    print(round(ar,3))
else :
    print('N/A')
