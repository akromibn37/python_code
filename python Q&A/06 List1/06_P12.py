q = list(input().strip())
n = int(input())
for i in range(n):
  cmd = input().split()
  if cmd[0] == 'in' : 
    q.insert(int(cmd[2]),cmd[1])
  elif cmd[0] == 'out' :
    q.pop(int(cmd[1]))
  elif cmd[0] == 'swap' :
    i = int(cmd[1])
    j = int(cmd[2])
    q[i],q[j] = q[j],q[i]
  print(''.join(q))
