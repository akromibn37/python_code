import numpy as np

def eval_poly(x,coef):
    Y = np.ndarray(coef.shape[0])
    Y[0] = 1
    Y[1:] = x
    Y = np.cumprod(Y)
    return np.dot(coef, Y)

exec(input().strip())
