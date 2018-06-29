f = open(input().strip())
command = f.readline().strip()
w = f.readline().strip()

for l in f:
  s,a,b = l.strip().split()
  a = int(a)
  b = int(b)
  
  if command == 'find':
    x = s.find(w,a,b)
  else:
    x = s.rfind(w,a,b)
  
  if x == -1:
    print('not found')
  else:
    before = after = ''
    if x != 0:
      before = s[x-1]
    if x+len(w) < len(s):
      after = s[x+len(w)]
    print(before+w+after)

f.close()