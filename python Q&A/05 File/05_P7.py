f = open(input().strip())
c = 0
for l in f:
    if l.strip() == '': c += 1
f.close()
print(c)
