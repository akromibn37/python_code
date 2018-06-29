import math

r = float(input())
g = float(input())
b = float(input())
h = 2*math.pi - math.acos(((r-g)+(r-b))/(2*math.sqrt((r-g)**2+(r-b)*(g-b))))
s = 1 - (3*r/(r+g+b))
i = (r+g+b)/3
print(h)
print(s)
print(i)
