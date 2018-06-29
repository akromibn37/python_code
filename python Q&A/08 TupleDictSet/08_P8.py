x1 = input().split()
x2 = input().split()
t = input().split()
out = []
for e in t:
  if e in x1 :
    out.append(x2[x1.index(e)])
  elif e in x2:
    out.append(x1[x2.index(e)])
  else:
    out.append(e)
print(' '.join(out))
