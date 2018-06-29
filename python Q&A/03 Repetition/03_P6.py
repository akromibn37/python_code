while True:
    s = int(input())
    if s == -1 : break
    g = "F"
    if s > 100 : g = "Error"
    elif s >= 80 : g = "A"
    elif s >= 75 : g = "B+"
    elif s >= 70 : g = "B"
    elif s >= 65 : g = "C+"
    elif s >= 60 : g = "C"
    elif s >= 55 : g = "D+"
    elif s >= 50 : g = "D"
    else : g = "F"
    print(g)
