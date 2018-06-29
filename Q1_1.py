import math
r = float(input().strip())
g = float(input().strip())
b = float(input().strip())
h = (math.pi*2) - math.acos(((r-g)+(r-b))/(2*(math.sqrt((math.pow(r-g,2)+((r-b)*(g-b)))))))
s = 1- ((3*r)/(r+g+b))
i = (r+g+b)/3
print(h) 
print(s)
print(i)