a,b,c = [float(e) for e in input().split()]
if a == 0 and b ==0 and c ==0:
    print("Roots are any numbers")
elif a ==0 and b == 0 and c!=0 :
    print("No roots exists")
elif a ==0 and b !=0 and c != 0:
    r1 = -(c/b)
    print ("{:.2f}".format(r1))
else:
    if b*b<4*a*c:
        print("Roots are complex numbers")
    elif b*b > 4*a*c :
        t = b*b - 4*a*c
        r1 = ((-1*b)+(t**0.5))/(2*a); tr1 = "{:.2f}".format(r1)
        r2 = ((-1*b)-(t**0.5))/(2*a); tr2 = "{:.2f}".format(r2)
        if tr1 != tr2 :
            if r1>=r2:
                print(tr2,tr1)
            elif r1<r2:
                print(tr1,tr2)
    elif b*b == 4*a*c:
        t = b*b - 4*a*c
        r1 = ((-1*b)+(t**0.5))/(2*a); tr1 = "{:.2f}".format(r1)
        print(tr1)