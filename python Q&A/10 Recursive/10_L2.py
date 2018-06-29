def x(n): # Logistic Map
    if n == 0 : return 0.01
    y = x(n-1)
    return 3*y*(1-y)
    
def M(n): # Motzkin number
  if n==0 or n==1 : return 1
  Mn = M(n-1)
  for k in range(n-1):
    Mn += M(k)*M(n-2-k)
  return Mn

def D(m,n): # Delannoy number 
  if m == 0 or n == 0 : return 1
  return D(m-1,n)+D(m-1,n-1)+D(m,n-1)

def S(n): # Schroder-Hipparchus number
  if n == 1 or n == 2 : return 1
  return ((6*n-9)*S(n-1)-(n-3)*S(n-2))//n

def d(n): # Number of Derangements
  if n == 0 : return 1
  return n*d(n-1)+(-1)**n    
    
exec(input().strip()) # do not remove this line
