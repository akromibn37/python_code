n = int(input())
d  = []
for k in range(n):
  d.append(input().strip())
c = 0
for k in range(n-1):
  for i in range(n-1):
    if len(d[i])<len(d[i+1]) :
      continue
    if len(d[i])==len(d[i+1]) and d[i] <= d[i+1] :
      continue
    d[i],d[i+1] = d[i+1],d[i]
    c += 1
print('\n'.join(d))
print(c)
