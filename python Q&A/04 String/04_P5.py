bits = input().strip()
n = 0
for c in bits:
    if c == "1" : n += 1
print(bits+str(n%2))
