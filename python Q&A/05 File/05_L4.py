f = open(input().strip())
n = int(input())
s = input().lower()
d = input()
if s[-1] == '\n' or s[-1] == '\r' : s = s[:-1]
if d[-1] == '\n' or d[-1] == '\r' : d = d[:-1]

for line in f:
    l0 = line.lower()
    if l0[-1]=='\n' or l0[-1]=='\r' : l0 = l0[:-1]
    out = ""
    p = 0
    k = l0.find(s,p)
    while k >= 0 and n > 0:
        out += line[p:k] + d 
        n -= 1
        p = k + len(s)
        k = l0.find(s,p)
    out += line[p:]
    print(out)        
f.close()
