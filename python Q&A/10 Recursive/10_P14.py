def reach(s,e,d):
  if s==e:
    return True
  if s not in d:
    return False
  for tt in d[s]:
    if reach(tt,e,d):
      return True
  return False

d = {}
n,start,end = [int(e) for e in input().split()]
for i in range(n):
  a,b = [int(e) for e in input().split()]
  if a not in d:
    d[a] = set()
  d[a].add(b)

if reach(start,end,d):
  print('yes')
else:
  print('no')
