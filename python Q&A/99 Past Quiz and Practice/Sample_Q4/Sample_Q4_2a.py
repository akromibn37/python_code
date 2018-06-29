import numpy as np

def H(m):
    if m == 1 : return np.array([[1]])
    h = H(m-1)
    n = 2**(m-1)
    hn = np.ndarray( (2*h.shape[0],2*h.shape[1]),dtype=int )
    hn[:n//2,:n//2] = hn[:n//2,n//2:] = hn[n//2:,:n//2] = h
    hn[n//2:,n//2:] = -h
    return hn

def P(n):
    if n == 1 : return 1
    return 3*P(n-1) + M(n-1)

def M(n):
    if n == 1 : return 0
    return 3*M(n-1) + P(n-1)

def S(n):
    if n == 1 : return 1
    return 2*S(n-1)
    
exec(input().strip()) # do not remove this line
