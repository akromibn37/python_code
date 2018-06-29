t = input().strip()
nv = 0
nc = 0
for c in t:
    c = c.upper()
    if c in "AEIOU" :
        nv += 1
    elif "A" <= c <= "Z" :
        nc += 1
print(nv, nc)
