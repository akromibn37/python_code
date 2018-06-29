while True:
    x = [float(e) for e in input().split()]
    if x[0] == -1 : break
    w,h = x[0],x[1]
    print(w/((h/100)**2))
