a1, b1, c1, = [int(e) for e in input().split()]
a2, b2, c2, = [int(e) for e in input().split()]
if a1==0 and b1==0 or a2==0 and b2==0 :
  print('no solution')
  exit(0)
if a1 == 0 and a2 != 0 or a1 != 0 and a2 == 0 :
  print('one solution')
  exit(0)
if b1 == 0 and b2 != 0 or b1 != 0 and b2 == 0 :
  print('one solution')
  exit(0)
if b1 == 0 and b2 == 0 :
  if c1/a1 == c2/a2:
    print('many solutions')
    exit(0)
  else:
    print('no solution')
    exit(0)
m1 = a1/b1; m2 = a2/b2
cc1 = c1/b1; cc2 = c2/b2
if m1 == m2 :
  if cc1 == cc2 :
    print('many solutions')
    exit(0)
  else:
    print('no solution')
    exit(0)
print('one solution')