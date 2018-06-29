l = [int(e) for e in input().split()]
a = set()
b = set()
for ll in l:
  if ll not in a:
    a.update({ll})
  elif ll in a and ll not in b:
    b.update({ll})
if len(a-b)!=0:
  print(min(a-b))
else:
  print("NONE")
