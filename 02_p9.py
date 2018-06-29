m,y = [int(e) for e in input().split()]
add=0

y = y-543
if ((y%4==0) and (y%100!=0)) or (y%400==0):
	add = 1

if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
	print('31')

elif m ==4 or m==6 or m==9 or m==11 :
	print('30')

else:
	b = 28+add
	print(b)
	