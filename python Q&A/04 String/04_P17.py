t = input().strip()
if t == 'soon' :
    print(0)
    exit(0)
    
sign = ''
if t[:3] == 'lop':
    sign = '-'
    t = t[4:]

th = 'soon nuengsong sam  see  ha   hok  jed  pad  kao  '
po = 'soonsip roeypun muensaenlarn'

k = t.find('-jood')
out = ''
if k >= 0:
    out = '.'
    d = t[k+len('-jood-'):] + '-'
    t = t[:k];
    k = d.find('-')
    p = 0
    while k >= 0:
        out += str(th.find(d[p:k])//5)
        p = k+1
        k = d.find('-',p)
        
t = t.replace('yee', 'song')
t = t.replace('sip-ed', 'sip-nueng')
t = t.replace('sip', 'nueng-sip')

k = t.find("-larn")
tm = ''
if k >= 0:
    tm = t[:k]
    if k+len('-larn') == len(t) :
        t = ''
    else:
        t = t[k+len('-larn-'):]

tm += '-soon-'
t += '-soon-'
d6 = 0
p = 0
k = tm.find('-')
while k >= 0:
    i = th.find(tm[p:k])//5
    p = k+1
    k = tm.find('-',p)
    if k < 0:break
    m = po.find(tm[p:k])//4
    if m < 0:
        p = k+1
        k = tm.find('-',p)
        if k < 0 : break
        m = po.find(tm[p:k])//4    
    d6 += i*10**m
    p = k+1
    k = tm.find('-',p)


d0 = 0
p = 0
k = t.find('-')
while k >= 0:
    i = th.find(t[p:k])//5
    p = k+1
    k = t.find('-',p)
    if k < 0:break
    m = po.find(t[p:k])//4
    if m < 0:
        p = k+1
        k = t.find('-',p)
        if k < 0 : break
        m = po.find(t[p:k])//4
    d0 += i*10**m
    p = k+1
    k = t.find('-',p)

d = str(d6*10**6 + d0)
o = ''
p = len(d)
while p-3 > 0:
    o = d[p-3:p] + ',' + o
    p -= 3
o = d[:p] + ',' + o
    
print(sign + o[:-1] +out)
