import numpy as np

#http://www.labri.fr/perso/nrougier/teaching/numpy.100/
def checker(n):
    Z = np.zeros((n,n),dtype=int)
    Z[1::2,::2] = Z[::2,1::2] = 1
    return Z

def collide(e,c):
    return c[ np.sum((c[:,:2]-e[:2])**2,axis=1) <= (c[:,2]+e[2])**2 ]

def matrix_chain_mult(M, order):
    R = M[order[0]].dot(M[order[1]])
    for i in range(2,len(order)):
        if order[i] < order[i-1]:
            R = M[order[i]].dot(R)
        else:
            R = R.dot(M[order[i]])
    return R

exec(input().strip())
