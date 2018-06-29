c = dict()
while True:
    x = input().split()
    if x[0] == '-1' : break
    for e in x[1:]:
        if e not in c :
            c[e] = set()
        c[e].add(x[0])
c1, c2 = input().split()
cc1 = c[c1] if c1 in c else set()
cc2 = c[c2] if c2 in c else set()
ns = len(cc1&cc2)
nu = len(cc1|cc2)
print(ns, (nu-ns), nu)
