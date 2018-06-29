import numpy as np

def to_polar(p):
    X,Y = p[:,0], p[:,1]
    rt1 = np.ndarray(p.shape)
    rt1[:,0] = np.sqrt(X**2+Y**2)
    rt1[:,1] = np.arctan2(Y,X)
    return rt1

def to_cartesian(p):
    R,T = p[:,0], p[:,1]
    xy1 = np.ndarray(p.shape)
    xy1[:,0] = R*np.cos(T)
    xy1[:,1] = R*np.sin(T)
    return xy1

def mandel( h, w, m ):
    y,x = np.ogrid[ -1.4:1.4:h*1j, -2:0.8:w*1j ]
    c = x+y*1j
    z = c
    dt1 = m + np.zeros(z.shape, dtype=int)
    for i in range(m):
        z = z**2 + c
        di = z*np.conj(z) > 2**2         
        dn = di & (dt1==m)  
        dt1[dn] = i                  
        z[di] = 2
    return dt1

def merge( dt, m ):
    x1 = dt[m,:]
    y1 = dt[:,m]
    xy1 = [[x1[k],y1[k]] for k in range(len(x1))]
    xy1 = np.array(xy1,float)
    return xy1
    
def main(): 
    h1,w1,m1 = [int(e) for e in input().split()]
    h2,w2,m2 = [int(e) for e in input().split()]

    dt1 = mandel(h1,w1,m1)
    xy1 = merge(dt1,m1)
    rt1 = to_polar(xy1)
    rt1[:,1] += 0.5
    xy1 = to_cartesian(rt1)

    dt2 = mandel(h2,w2,m2)
    xy2 = merge(dt2,m2)
    xy2[:,1] += 0.5
    xy2 = to_cartesian(xy2)

    print(np.sum(xy1.dot(xy2.T)))

exec(input().strip()) # do not remove this line

