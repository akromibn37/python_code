n = int(input())
found = False
for x in range(n):
    for y in range(x,n):
        if x**2 + y**2 == n:
            print(x, y)
            found = True
if not found:
    print("No solution")
