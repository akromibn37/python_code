t = input().strip()
x,y = 0,0
for e in t:
    if e == 'U':
        y += 1
    elif e == 'D':
        if y > 0 : y -= 1
    elif e == 'L':
        if x > 0 : x -= 1
    elif e == 'R':
        x += 1
print('('+str(x)+','+str(y)+')')
