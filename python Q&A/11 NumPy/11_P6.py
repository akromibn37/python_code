import numpy as np

def scale(img, c) :
    out = np.ndarray((img.shape[0]//c, img.shape[1]//c))
    M = np.ones((c,c))/(c**2)
    for i in range(out.shape[0]):
        for j in range(out.shape[1]):
            out[i,j] = np.sum(img[c*i:c*(i+1),c*j:c*(j+1)]*M)
    return out

def read_img():
    row, col = [int(e) for e in input().split()]
    img = np.ndarray((row,col))
    for i in range(row):
        img[i] = [float(e) for e in input().split()]
    return img

def show_output(out):
    for i in range(out.shape[0]):
        print(" ".join([str(e) for e in out[i]]))

img = read_img()
c = int(input())
out = scale(img, c)
show_output(out)
