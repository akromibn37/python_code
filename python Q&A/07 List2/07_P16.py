r,c = [int(e) for e in input().split()]

A = []
for i in range(r):
  A.append([int(e) for e in input().split()])

B = []
for i in range(r):
  B.append([int(e) for e in input().split()])

for i in range(r):
  s = ""
  for j in range(c):
    s += str(A[i][j]+B[i][j])+" "
  print(s)
