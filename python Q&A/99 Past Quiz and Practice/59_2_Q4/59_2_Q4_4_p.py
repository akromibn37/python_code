import numpy as np

def decode(c, base, oddonly) :
    x = np.array([[base**i for i in range(c.shape[0]-1,-1,-1)]]).dot(c)
    x = np.array(x[0])
    if oddonly: return x[1::2]
    return x

exec(input().strip()) # do not remove these three lines
exec(input().strip()) #
exec(input().strip()) #