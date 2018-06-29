n = int(input())

for i in range(n//2):
    dot = (n//2-1-i)
    sharp = n-2*dot
    pic = '.'*dot + '#'*sharp + '.'*dot
    print(pic+'.'+pic)

for i in range(n//2-2):
    print('#'*(2*n+1))

for i in range(n+1):
    sharp = 2*n+1-2*i
    print('.'*i + '#'*sharp + '.'*i)
