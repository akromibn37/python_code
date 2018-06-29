upper, n = [int(x) for x in input().split()]
d = []
for i in range(n):
    d.append([int(x) for x in input().split()])
sum = 0
for i in range(n):
   for j in range(i,n) if upper else range(0,i+1):
        sum += d[i][j]
print(sum)
