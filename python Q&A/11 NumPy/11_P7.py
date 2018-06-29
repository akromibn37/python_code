import numpy as np

n = int(input())
A = np.ndarray((n,n))
for k in range(n):
    A[k] = np.array([int(e) for e in input().split()])

B = np.zeros_like(A)
C = np.identity(n)
for k in range(n-1):
    C = C.dot(A)
    B = B + C
B = np.sign(B)
for k in range(n):
    print(' '.join([str(int(e)) for e in B[k]]))
