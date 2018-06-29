op = input().strip()
r = int(input())
s = ''
for i in range(r):
    ss = input().strip()
    s += ss
    if i == 0:
        c = len(ss)
    elif len(ss) != c:
        print('Invalid size')
        exit(0)

if op == '90':
    for i in range((r-1)*c,r*c):
        print(s[i::-c])
        
if op == 'flip':
    for i in range(r):
        print(s[i*c:i*c+c][::-1])

if op == '180':
    for i in range(r-1,-1,-1):
        print(s[i*c:i*c+c][::-1])
