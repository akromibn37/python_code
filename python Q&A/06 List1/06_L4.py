x = [int(e) for e in input().split()]
r = len(x)//2 + 1
s = x[r-1]
for i in range(1,r):
  x = [int(e) for e in input().split()]
  s += sum(x[r-i-1:r+i])
print(s)
