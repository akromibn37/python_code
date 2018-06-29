d = int(input())
m = int(input())
y = int(input())
add = 0
sum=0
y = y-543
if ((y%4==0) and (y%100!=0)) or (y%400==0) :
	add = 1
if m>1 :
	sum+=31
if m>2 :
	sum+=28+add
if m>3 :
	sum+=31
if m>4 :
	sum+=30
if m>5 :
	sum+=31
if m>6 :
	sum+=30
if m>7 :
	sum+=31
if m>8 :
	sum+=31
if m>9 :
	sum+=30
if m>10 :
	sum+=31
if m>11 :
	sum+=30

print(sum+d)
	
	