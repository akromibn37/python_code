s = 0
x = int(input())
while x > 0:
    if x % 2 == 0:
        s += x
    x = int(input())
print(s)
