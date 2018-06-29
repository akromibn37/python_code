x1,y1,r1,x2,y2,r2 = [float(e) for e in input().split()]
dd = ((x1-x2)**2 + (y1-y2)**2)**0.5
rr = (r1+r2)
if abs(dd-rr) < rr*1e-5:
    print(1)
elif dd < rr:
    print(2)
else:
    print(3)
