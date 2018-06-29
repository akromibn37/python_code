import numpy as np

def fib(n, k):
  if n == 0 : return 0
  A = np.array([[0,1],[1,1]])
  f = np.identity(2,int)
  for i in range(n):
    f = (f @ A) % k
  return f[0,1]
  
n,k = [int(e) for e in input().split()]
print(fib(n,k))
