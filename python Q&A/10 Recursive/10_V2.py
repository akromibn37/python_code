def h(n): # Tower of Hanoi
  if n == 0 : return 0
  return 2*h(n-1)+1
  
def gcd(x,y): # Greatest Common Divisor
  if y == 0 : return x
  return gcd(y,x%y)
  
def J(n,k): # Josephus Problem
  if n==1 : return 0
  return (J(n-1,k)+k) % n

def C(n): # Catalan Number
  if n == 0: return 1
  s = 0
  for k in range(n):
    s += C(k)*C(n-1-k)
  return s

def f(n): # Fibonacci Number
  if n < 2 : return n
  if n%2 == 0 :
    m = n//2
    return (2*f(m-1)+f(m))*f(m)
  else:
    m = n//2 + 1
    return f(m)**2 + f(m-1)**2
    
def F(n): # Female sequence
  if n == 0 : return 1
  return n - M(F(n-1))

def M(n): # Male sequence
  if n == 0 : return 0
  return n-F(M(n-1))

def A(m,n): # Ackermann Number
  if m == 0 : return n+1
  if n == 0 : return A(m-1,1)
  return A(m-1,A(m,n-1))
  
exec(input().strip()) # do not remove this line
