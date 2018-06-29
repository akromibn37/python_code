def det3(m):
    # รับ input m ในรูปแบบ [[1,2,3],[4,5,6],[7,8,9]]
    a = m[0][0]*m[1][1]*m[2][2]
    b = m[0][1]*m[1][2]*m[2][0]
    c = m[0][2]*m[1][0]*m[2][1]
    d = m[0][2]*m[1][1]*m[2][0]
    e = m[0][0]*m[1][2]*m[2][1]
    f = m[0][1]*m[1][0]*m[2][2]
    return a+b+c-d-e-f

def det4(m):
    d = 0
    s = 1
    for k in range(4):
        m3 = [m[1][0:k]+m[1][k+1:],
              m[2][0:k]+m[2][k+1:],
              m[3][0:k]+m[3][k+1:]]
        d += s*m[0][k]*det3(m3)
        s *= -1
    return d

matrix = []
for i in range(4):
    matrix.append([int(e) for e in input().split()])
print(det4(matrix))
