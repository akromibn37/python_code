m,y = [int(e) for e in input().split()]
y -= 543
if m==4 or m==6 or m==9 or m==11:
    d = 30
elif m != 2:
    d = 31
elif (y%4 == 0 and y%100 != 0) or y%400==0:
    d = 29
else:
    d = 28
print(d)
