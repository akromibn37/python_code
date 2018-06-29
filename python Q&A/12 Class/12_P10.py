class rational:
 def __init__(self, n, d):
  g = gcd(n,d)
  self.n = n//g
  self.d = d//g
 def __str__(self):
  return str(self.n) + "/" + str(self.d)
 def __lt__(self, rhs):
  return float(self) < float(rhs)
 def __float__(self):
  return self.n / self.d
 def __mul__(self, rhs):
  return rational( self.n*rhs.n,self.d*rhs.d )

 def __add__(self,rhs):
   return rational( self.n*rhs.d+rhs.n*self.d,self.d*rhs.d )

 def __sub__(self,rhs):
   return rational( self.n*rhs.d-rhs.n*self.d,self.d*rhs.d )

 def __truediv__(self,rhs):
   return rational( self.n*rhs.d,self.d*rhs.n )

def gcd(a,b):
  if a%b==0: return b
  return gcd(b,a%b)

t, n1, d1, n2, d2 = input().split()
r1 = rational(int(n1),int(d1)); r2 = rational(int(n2),int(d2))
if t == '+' : print(str(r1 + r2))
elif t == '-' : print(str(r1 - r2))
elif t == '/' : print(str(r1 / r2))
else : print(str(r1 * r2))
