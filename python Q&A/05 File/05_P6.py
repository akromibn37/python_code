f1 = open(input().strip())
f2 = open(input().strip())

for l1 in f1:
    n = int(l1)
    s = 0
    for i in range(n):
        s += float(f2.readline())
    print(s/n)

f1.close()
f2.close()
