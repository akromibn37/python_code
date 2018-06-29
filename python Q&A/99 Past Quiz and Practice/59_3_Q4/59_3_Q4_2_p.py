def p(n):
  if 0<=n<=2: return 1
  return p(n-2)+p(n-3)

def m(n):
  if n==1 or n==2: return 1
  x = m(n-2)
  return m(x)+m(n-x)

def e(n):
  if n==2 or n==3: return 1
  s = 0
  for k in range(1,n-1):
    s += e(k+1)*e(n-k)
  return s
  
def s(n,k):
  if n==0: return 2
  x = s(n-1,k)
  return (x**2-x+1)%k
  
exec(input().strip())