d = int(input())
m = int(input())
y = int(input())

y -= 543
if (y % 4 == 0 and y % 100 != 0) or  y % 400 == 0 :
	m2 = 29
else :
    m2 = 28	
if m == 1 :
   nd = d
if m == 2 :
   nd = 31 + d
if m == 3 :
   nd = 31 + m2 + d
if m == 4 :
   nd = 31 + m2 + 31 + d
if m == 5 :
   nd = 31 + m2 + 31 + 30 + d
if m == 6 :
   nd = 31 + m2 + 31 + 30 + 31 + d
if m == 7 :
   nd = 31 + m2 + 31 + 30 + 31 + 30 + d
if m == 8 :
   nd = 31 + m2 + 31 + 30 + 31 + 30 + 31 + d
if m == 9 :
   nd = 31 + m2 + 31 + 30 + 31 + 30 + 31 + 31 + d
if m == 10 :
   nd = 31 + m2 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + d
if m == 11 :
   nd = 31 + m2 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + d
if m == 12 :
   nd = 31 + m2 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + d
print(nd)


 