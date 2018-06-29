d0 = [int(e) for e in input().split()]
d1 = [int(e) for e in input().split()]
c = input().strip()
out = []

if c == 'z':
    m = min(len(d0),len(d1))
    for i in range(m):
        out += [d0[i],d1[i]]
    if len(d0)<len(d1):
        out += d1[m:]
    if len(d1)<len(d0):
        out += d0[m:]

else:
    i = j = 0
    while i<len(d0) and j<len(d1):
        if d0[i]<d1[j]:
            out += [d0[i]]
            i += 1
        else:
            out += [d1[j]]
            j += 1
    for k in range(i,len(d0)):
        out += [d0[k]]
    for k in range(j,len(d1)):
        out += [d1[k]]

print(out)
