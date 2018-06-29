import math
a = float(input())
b = float(input())
c = float(input())
c = math.radians(c)
x = math.pow(a,2)+math.pow(b,2)-(2*a*b*math.cos(c))
co = math.pow(x,1/2)
print("c =",co,"cm.")