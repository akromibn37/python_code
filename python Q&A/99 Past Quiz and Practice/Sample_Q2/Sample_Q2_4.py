t = input().strip().lower()
m = 1
mp = t[0]
for i in range(len(t)):
    for j in range(i,len(t)):
        a = t[i:j+1];
        if a == a[::-1] :
            if len(a) > m:
                mp = a
                m = len(a)
            if len(a) == m:
                if a < mp : mp = a
print(mp)
