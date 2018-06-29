d = [int(e) for e in input().split(',')]
ans = 0
sign = 0
for i in range(len(d)):
  if d[i] < 0 and sign == 0 :
    sign = -1
    ans += 1
  elif d[i] >= 0:
    sign = 0
print(ans)
