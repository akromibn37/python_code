def nextEven(f):
    n = int(f)
    return n+2 if n%2 == 0 else n+1

def nextOdd(f):
    n = int(f)
    return n+1 if n%2 == 0 else n+2

while True:
    x = float(input())
    if x < 0:
        break
    even = nextEven(x)
    odd = nextOdd(x)
    print( (even, odd) )

