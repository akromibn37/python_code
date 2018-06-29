def fac(n): 
  return str(n) + '!'
def oneterm(x,n): 
  return str(x)+'**'+str(n)+'/'+fac(n)
def sin(x,n): 
  out = str(x)
  k = 3
  sign = '-'
  for i in range(n-1):
    out += ' ' + sign + ' ' + oneterm(x,k)
    k += 2
    sign = '-' if sign == '+' else '+'
  return out
    
exec(input().strip())
