import math

bd, bm, by, d, m, y = [int(e) for e in input().split()]

# day of year 1

feb = 28
all = 365
if (by-543)%400==0 or ((by-543)%4==0 and (by-543)%100!=0):
    feb = 29
    all = 366
d1 = bd
if bm>1: d1 += 31
if bm>2: d1 += feb
if bm>3: d1 += 31
if bm>4: d1 += 30
if bm>5: d1 += 31
if bm>6: d1 += 30
if bm>7: d1 += 31
if bm>8: d1 += 31
if bm>9: d1 += 30
if bm>10: d1 += 31
if bm>11: d1 += 30

# day of year 2

feb = 28
if (y-543)%400==0 or ((y-543)%4==0 and (y-543)%100!=0):
    feb = 29
d2 = d
if m>1: d2 += 31
if m>2: d2 += feb
if m>3: d2 += 31
if m>4: d2 += 30
if m>5: d2 += 31
if m>6: d2 += 30
if m>7: d2 += 31
if m>8: d2 += 31
if m>9: d2 += 30
if m>10: d2 += 31
if m>11: d2 += 30

d1 = all-d1+1
d2 -= 1

dd = d1+d2+(y-by-1)*365
p1 = math.sin(2*math.pi*dd/23)
p2 = math.sin(2*math.pi*dd/28)
p3 = math.sin(2*math.pi*dd/33)

p1 = "{:.2f}".format(p1)
p2 = "{:.2f}".format(p2)
p3 = "{:.2f}".format(p3)

print(dd,p1,p2,p3)

