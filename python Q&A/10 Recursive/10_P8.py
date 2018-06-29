def gcd(x,y):
  if x >= y and x%y==0: return y
  return gcd(y, x%y)

x,y = [int(e) for e in input().split()]
print(gcd(x,y))
