n = int(input())
nxt = [0]*n
for i in range(n):
  nxt[i] = int(input())
d = [0]*n
d[0] = 1
p = 0
for i in range(1,n): 
  d[i] = nxt[p]
  p = nxt[p]-1
print(' '.join( [str(e) for e in d] ))
