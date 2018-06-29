import math
a = float(input())
b = float(input())
D = float(input())
c = math.radians(D)
area = 1/2*a*b*math.sin(c)
print("area =", area, "(sq cm)")
