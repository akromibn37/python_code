s = input().strip()
x = [int(e) for e in s.split()]
m = input().strip()
if m == 'a':
    i = 0
    while i < len(x)-1:
        j = 0
        while j < len(x)-1:
            if x[j] > x[j+1]:
                x[j],x[j+1] = x[j+1],x[j]
            j+=1
        i+=1
else:
    i = 0
    while i < len(x)-1:
        j = 0
        while j < len(x)-1:
            if x[j] < x[j+1]:
                x[j],x[j+1] = x[j+1],x[j]
            j+=1
        i+=1
print(x)    
