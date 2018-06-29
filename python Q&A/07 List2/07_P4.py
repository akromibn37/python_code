d = []
e = int(input())
while e != -1:
    d.append(e)
    e = int(input())
d.sort()
e = d[len(d)//2]
if d.count(e) > len(d)//2 :
    print(e)
else:
    print("Not found")

