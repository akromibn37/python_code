import numpy as np

def fib(n,k):
    A = np.array([[0,1],[1,1]])
    if n == 1 : return A
    f1 = fib(n//2,k)
    f1 = (f1 @ f1) % k
    if n%2 == 1 : f1 = (A @ f1) % k
    return f1
  
n,k = [int(e) for e in input().split()]
print(fib(n,k)[0,1])
