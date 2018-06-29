d = [int(e) for e in input().split()]
player = [0]*2
turn = 0
while len(d) > 0:
  if d[0] > d[-1]:
    player[turn] += d[0]
    d = d[1:]
  else:
    player[turn] += d[-1]
    d = d[:-1]
  turn = 1 - turn
print(player[0])
print(player[1])
if s[0] > s[1]:
  print(1)
elif s[1] > s[0]:
  print(2)
else:
  print(0)
