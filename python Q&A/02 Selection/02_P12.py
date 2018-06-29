a,x = [int(e) for e in input().split()]
b,y = [int(e) for e in input().split()]
if x>b-y:
    print(x-(b-y),b)
else:
    print(0,x+y)
