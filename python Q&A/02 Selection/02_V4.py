d = int(input())
m = int(input())
y = int(input())
y = y-543

feb = 28
if (y%4==0 and y%100!=0) or y%400==0:
    feb = 29

if m==1:
    x = d
elif m==2:
    x = 31+d
elif m==3:
    x = 31+feb+d
elif m==4:
    x = 31+feb+31+d
elif m==5:
    x = 31+feb+31+30+d
elif m==6:
    x = 31+feb+31+30+31+d
elif m==7:
    x = 31+feb+31+30+31+30+d
elif m==8:
    x = 31+feb+31+30+31+30+31+d
elif m==9:
    x = 31+feb+31+30+31+30+31+31+d
elif m==10:
    x = 31+feb+31+30+31+30+31+31+30+d
elif m==11:
    x = 31+feb+31+30+31+30+31+31+30+31+d
else:
    x = 31+feb+31+30+31+30+31+31+30+31+30+d
print(x)
