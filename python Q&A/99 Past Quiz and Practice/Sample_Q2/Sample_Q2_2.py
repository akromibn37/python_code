b = int(input())
start, stop, step = input().split()

start = start[::-1]
stop = stop[::-1]
step = step[::-1]

s1 = 0
for i in range(len(start)):
  s1 += int(start[i])*b**i

s2 = 0
for i in range(len(stop)):
  s2 += int(stop[i])*b**i

s3 = 0
for i in range(len(step)):
  s3 += int(step[i])*b**i

for a in range(s1,s2,s3):
  out = ""
  while a > 0:
    out = str(a % b) + out
    a //= b
  if out == "" : out = "0"
  print(out)
