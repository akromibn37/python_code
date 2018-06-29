y = int(input())
y -= 543
if (y%100 != 0 and y%4 == 0) or y%400 == 0 :
    print(29)
else :
    print(28)
