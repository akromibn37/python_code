import numpy as np
t = np.array([[15,3.78],
              [29,2.0],
              [10,2.5],
              [25,2.85],
              [30,3.96]])
logit = -3.98 + 0.2*t[:,0] + 0.5*t[:,1]
p = 1/(1+np.exp(-logit))
n = int(input()) - 1
if 0 <= n < p.shape[0] :
    print(p[n]>0.5)
else:
    print("Error")
