import numpy as np
n = int(input())
p = []
for i in range(n):
    p += [int(input().split()[1])]
c = []
for i in range(n):
    c += [int(e) for e in input().split()[1:]]
x = np.array(p).dot(np.array(c))
for i in x:
    print(float(i))
