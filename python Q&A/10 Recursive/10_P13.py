def gen(s):
  if s=='':
    return set({''})
  x = gen(s[1:])
  if s[0] == s[0].upper():
    return x.union(set([s[0]+e for e in x]))
  return set([s[0]+e for e in x])

z = sorted(gen(input().strip()))
for zz in z:
  if zz!='':
    print(zz)

