def reach(s,e,d,path):
  if s==e:
    print(" -> ".join([str(e) for e in path]))
    return True
  if s not in d:
    return False
  x = False
  for tt in sorted(d[s]):
    if reach(tt,e,d,path+[tt]):
      x = True
  return x

d = {}
n,start,end = [int(e) for e in input().split()]
for i in range(n):
  a,b = [int(e) for e in input().split()]
  if a not in d:
    d[a] = set()
  d[a].add(b)

if not reach(start,end,d,[start]):
  print('no')
