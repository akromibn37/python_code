t = input().strip()
a = input().strip()
b = input().strip()
out = ''
for e in t:
    if e in a:
        out += b[a.find(e)]
    elif e in b:
        out += a[b.find(e)]
    else:
        out += e
print(out)
