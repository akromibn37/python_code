r,c = [int(e) for e in input().split()]

row = [[] for i in range(r)]
col = [[] for i in range(c)]

for i in range(r):
  x = [int(e) for e in input().split()]
  for j in range(c):
    row[i].append(x[j])
    col[j].append(x[j])

ans = -1
for i in range(r):
  for j in range(c):
    if min(row[i])==max(col[j]):
      ans = min(row[i])
print(ans)

