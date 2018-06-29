import numpy as np

def read_matrix():
    r,c = [int(e) for e in input().split()]
    m = [[int(e) for e in input().split()] for i in range(r)]
    return np.array(m)

def dot_row_column(m):
    return m.dot(m)

def mul_submatrix(m,n):
    k = n.shape[0]
    p = np.ndarray(m.shape,dtype=int)
    for i in range(0,p.shape[0],k):
        for j in range(0,p.shape[1],k):
            p[i:i+k,j:j+k] = m[i:i+k,j:j+k].dot(n)
    return p

def resize(m,a,b):
    r = m.shape[0]
    c = m.shape[1]
    rr = a//r*r + r
    cc = b//c*c + c
    p = np.ndarray((rr,cc),dtype=int)
    for i in range(rr//r):
        for j in range(cc//c):
            p[i*r:(i+1)*r,j*c:(j+1)*c] = m
    return p[:a,:b]
            
exec(input().strip()) # do not remove this line
