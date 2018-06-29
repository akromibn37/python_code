import math

a = float(input())
b = float(input())
d = float(input())
c = math.radians(d)
area = (a*b*math.sin(c))/2
print("area =",area,"(sq cm)")
