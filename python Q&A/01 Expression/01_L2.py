import math
a = float(input())
b = float(input())
D = float(input())
C = math.radians(D)
c = math.sqrt(a*a + b*b - 2*a*b*math.cos(C))
print("c =", c, "cm.")
