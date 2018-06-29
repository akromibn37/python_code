fin = open(input().strip())
a = input().strip()
b = input().strip()
c = input().strip()
ca = cb = cc = 0
for line in fin:
    for x in line:
        if x == a : ca += 1
        if x == b : cb += 1
        if x == c : cc += 1

if ca > cb > cc : print(a+b+c)
if ca > cc > cb : print(a+c+b)
if cb > ca > cc : print(b+a+c)
if cb > cc > ca : print(b+c+a)
if cc > ca > cb : print(c+a+b)
if cc > cb > ca : print(c+b+a)
