def tiling(n, c):
  if n == 1: return 1
  if c == 'R' or c == 'B' :
    return tiling(n-1,'G')+tiling(n-1,'R')+tiling(n-1,'B')
  else:
    return tiling(n-1,'R')+tiling(n-1,'B')

N = int(input())
print(tiling(N,'G')+tiling(N,'R')+tiling(N,'B'))
