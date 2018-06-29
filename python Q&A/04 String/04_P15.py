t = list(input().strip())
out = ''
for k in range(len(t)):
    if t.count(t[k]) == 1:
        out += t[k]
    elif t.count(t[k]) > 1 and t[0:k].count(t[k]) == 1:
        out += t[k]
print(out)
