import numpy as np

n = int(input())
input()
input()
input()
x = np.array([[int(e) for e in input().split(",")] \
             for i in range(n-3)])
s = np.sum(x[:,1:],axis=1)
print("\n".join([str(float(e)) for e in s]))
