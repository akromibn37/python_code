s = input().strip()
ss = '0'
for c in s:
    if c=='-':
        ss += '+'
    ss += c

ans = 0
p = ss.find('+')
while p != -1:
    ans += int(ss[:p])
    ss = ss[p+1:]
    p = ss.find('+')

ans += int(ss)
print(ans)
