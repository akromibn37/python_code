m,n,p = [int(e) for e in input().split()]
A = []; B = []
for i in range(m):
  L = [int(e) for e in input().split()]
  A[len(A):] = L
  
for i in range(n):
  L = [int(e) for e in input().split()]
  B[len(B):] = L

C = []
for i in range(m*p):
  X = A[i//p*n:i//p*n+n]
  Y = [B[j] for j in range(len(B)) if i%p == j%p]
  C.append(sum([X[k]*Y[k] for k in range(len(X))]))

for i in range(m):
  s = ''
  for j in range(p):
    s += str(C[i*p+j]) + ' '
  print(s)
