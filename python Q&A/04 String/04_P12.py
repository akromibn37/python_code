t = input().strip().lower()
t = t.replace(' ','')
if t == t[::-1]:
    print('yes')
else:
    print('no')
