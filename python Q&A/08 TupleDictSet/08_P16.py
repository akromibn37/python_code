n = int(input())
s1 = s2 = set()
for k in range(n):
  s =  {int(e) for e in input().split()}
  if k == 0: s2 = set(s)
  s1 = s1 | s
  s2 = s2 & s
print(len(s1))
print(len(s2))
