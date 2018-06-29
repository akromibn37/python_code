a = input().strip()
b = input().strip()
az = 'abcdefghijklmnopqrstuvwxyz'
AZ = az.upper()
azAZ = az + AZ
out = ''
for e in azAZ:
    if e in a and e in b :
        out += e + ' '
if out == '':
    print('NONE')
else:
    print(out)
