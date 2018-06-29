a = input().strip()
b = input().strip()
a1 = a.lower()
b1 = b.lower()
alpha = 'abcdefghijklmnopqrstuvwxyz'
aa = ''
for e in a1:
    if e in alpha: aa += e
bb = ''
for e in b1:
    if e in alpha: bb += e

if len(aa) != len(bb):
    print(a,b)
    exit(0)

for e in aa:
    caa = 0
    for d in aa:
        if e == d : caa+=1
    cbb = 0
    for d in bb:
        if e == d : cbb+=1
    if caa != cbb:
        print(a,b)
        exit(0)

print(a)
