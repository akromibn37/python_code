f1 = open(input().strip())
f2 = open(input().strip())

for l1 in f1:
    l2 = f2.readline()
    print(l2.strip() in l1.strip())
f1.close()
f2.close()
