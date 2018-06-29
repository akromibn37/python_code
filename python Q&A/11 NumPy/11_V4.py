import numpy as np

def read_square_matrix():
    d = [int(e) for e in input().split()]
    m = [d]
    for k in range(len(d)-1):
        m.append([int(e) for e in input().split()])
    return np.array(m)

def min_in_each_row(m):
    return np.min(m,axis=1)

def max_in_each_column(m):
    return np.max(m,axis=0)

def diff_of_sums_of_two_diags(m):
    I = np.identity(m.shape[0],int)
    return abs(np.sum(m*I) - np.sum(m*I[::-1,:]))

def halve(m):
    a = m[::,::2]+m[::,1::2]
    return a[::2,::]+a[1::2,::]
    
exec(input().strip())
