pages = dict()
users = dict()
for k in range(int(input())):
  x = input().split()
  if x[0] not in pages : pages[x[0]] = set()
  pages[x[0]].update(set(x[1:]))
  for p in x[1:]:
    if p not in users: users[p] = set()
    users[p].add(x[0])

while True:
  x = input().split()
  if len(x) == 1 : break
  cmd = x[0]+' '+x[1]
  if cmd == 'common page' :
    p = pages[x[2]] if x[2] in pages else set()
    for u in x[3:]:
      p = p & (pages[u] if u in pages else set())
    print(len(p))
  elif cmd == 'common user' :
    u = users[x[2]] if x[2] in users else set()
    for p in x[3:]:
      u = u & (users[p] if p in users else set())
    print(len(u))
  elif cmd == 'similar page' :
    pp = x[2]
    out = []
    uu = users[pp] if pp in users else set()
    for p in users:
        if p == pp : continue
        u = users[p]
        out.append( (-(len(u & uu)/len(u | uu)),p) )
    print(min(out)[1])
  elif cmd == 'similar user' :
    uu = x[2]
    out = []
    pp = pages[uu] if uu in pages else set()
    for u in pages:
        if u == uu : continue
        p = pages[u]
        out.append( (-(len(p & pp)/len(p | pp)),u) )
    print(min(out)[1])
