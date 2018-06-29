d,m,y = [int(e) for e in input().split()]
t = input().strip()
if y < 2558 :
    print('Invalid year')
elif not (1 <= m <= 12) :
    print('Invalid month')
else :
    y -= 543
    if m == 2 :
        nm = 28
        if y%400==0 or (y%4==0 and y%100!=0) :
            nm = 29    
    elif m == 4 or m == 6 or m == 9 or m == 11 :
        nm = 30
    else :
        nm = 31
    if not( 1<= d <= nm ):
        print('Invalid date')
    elif not (t == 'E' or t == 'Q' or t == 'N' or t == 'F') :
        print('Invalid delivery type')
    else:
        if t == 'E' : # express next-day delivery
            d2 = d + 1
        elif t == 'Q' : # quick 3-day delivery
            d2 = d + 3
        elif t == 'N' : # normal 7-day delivery
            d2 = d + 7
        else : # free 14-day delivery
            d2 = d + 14
        m2 = m
        y2 = y
        if d2 > nm :
            d2 = d2 - nm
            m2 += 1
            if m2 > 12 :
                m2 = 1
                y2 += 1
        print('delivered on ' + str(d2) + '/' + str(m2) + '/' + str(y2+543))
