f = open("data.txt")
n = int(input())
i = 0
for line in f:
    k = line.find('Name: ')
    if k >= 0:
        name = line[k+len('Name: '):]
        i += 1
        if i == n : break
f.close()
if i == n :
    print(name)
else:
    print('Not Found')
