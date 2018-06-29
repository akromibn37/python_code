import numpy as np

def all_pair_distances(p):
    x = p[:,0]
    y = p[:,1]
    X = np.array([x])
    Y = np.array([y])
    dx = (X - X.T)
    dy = (Y - Y.T)
    d = np.sqrt(dx**2 + dy**2)
    return d
    
exec(input().strip())
