s = 0
n = 0
while True:
    d = float(input())
    if d == -1 : break
    s += d
    n += 1
if n == 0 :
    print("No Data")
else:
    print(s/n)
