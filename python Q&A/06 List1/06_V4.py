fin = open(input().strip())
d = []
for line in fin:
    f,p = line.split()
    found = False
    for i in range(len(d)):
        if f == d[i][0] :
            d[i][1].append(p)
            found = True
            break
    if not found:
        d.append([f,[p]])
print(d)
s = [len(p) for a,p in d]
print("The most favorite fruit is ", d[s.index(max(s))][0])
