n = int(input())
if n == 0 :
    print("No Data")
else:
    s = 0
    for i in range(n):
        s += float(input())
    print( s/n )
