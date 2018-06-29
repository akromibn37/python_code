stack = []
while True:
  c = input().split()
  if c[0] == 'end' : break
  if c[0] == 'return':
    stack.append(' '.join(c[1:]))
    print(len(stack))
  elif c[0] == 'shelf':
    if len(stack)==0 :
      print('no book')
    else:
      print(stack[-1])
      stack.pop(len(stack)-1)
  elif c[0] == 'top':
    if len(stack)==0 :
      print('no book')
    else:
      print(stack[-1])
  elif c[0] == 'list':
      print(stack)
