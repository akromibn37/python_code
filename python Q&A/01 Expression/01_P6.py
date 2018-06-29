a1,b1,c1 = [float(e) for e in input().split()]
a2,b2,c2 = [float(e) for e in input().split()]
y = (c2*a1 - c1*a2)/(a2*b1 - a1*b2)
x = (c2*b1 - c1*b2)/(b2*a1 - b1*a2)
print(x,y)
