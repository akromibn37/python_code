a,b,c = [int(e) for e in input().split()]
if a+b<=c or b+c<=a or a+c<=b :
	print("NO")
else :
	print("YES")
