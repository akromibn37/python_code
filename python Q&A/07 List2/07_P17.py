d = []
while True:
    x = input().split()
    if len(x) == 1: break
    d.append((-float(x[1]), int(x[0])))
d.sort()
rank = 1
id = int(x[0])
for i in range(len(d)):
    if d[i][1] == id :
        print(rank)
        break
    rank += 1
else:
    print('Not Found')
