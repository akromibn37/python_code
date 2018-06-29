t = input().strip()
a = input().strip()
b = input().strip()
out = ''
for e in t:
    if e == a : out += b
    elif e == b : out += a
    else: out += e
print(out)
