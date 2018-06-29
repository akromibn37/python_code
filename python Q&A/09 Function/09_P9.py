def isSevenUp(x):
  return x % 7 == 0 or '7' in str(x) 
  
def nextSevenUp(x):
  x += 1
  while not isSevenUp(x) :
    x += 1
  return x
 
def prevSevenUp(x):
  x -= 1
  while not isSevenUp(x):
    x -= 1
  return x
 
f,x = input().strip().split()
x = int(x)
if f == 'isSevenUp': print(isSevenUp(x))
elif f == 'nextSevenUp': print(nextSevenUp(x))
elif f == 'prevSevenUp': print(prevSevenUp(x))
