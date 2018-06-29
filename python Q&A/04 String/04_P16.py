t = input().strip()

sign = ''
if t[0]=='-':
    t = t[1:]
    sign = 'lop-'

k = t.find('.')
d = ''
if k >= 0:
    d = t[k+1:]
    t = t[:k]
    
t = t.replace(',','')

tm = ''
if len(t) > 6 :
    tm = t[:-6]
    t = t[-6:]

th = 'soon nuengsong sam  see  ha   hok  jed  pad  kao  '
po = '    sip roeypun muensaenlarn'

t1 = ''
for i,c in enumerate(t[::-1]):
    if c == '0' : continue
    k = int(c)*5
    t1 = th[k:k+5].strip() + '-' + po[i*4:i*4+4].strip() + \
          ('-' if i > 0 else '') + t1
t1 = t1[:-1]

t2 = ''
for i,c in enumerate(tm[::-1]):
    if c == '0' : continue
    k = int(c)*5
    t2 = th[k:k+5].strip() + '-' + po[i*4:i*4+4].strip() + \
         ('-' if i > 0 else '') + t2
    
out = t1    
if t2 == '' :
    if t1 == '' : out = 'soon'
else:
    out = t2[:-1] + '-larn'
    if t1 != '' : out = out + '-' + t1

if out[-5:] == '-soon' : out = out[:-5]
out = out.replace('song-sip', 'yee-sip')
out = out.replace('nueng-sip', 'sip')
out = out.replace('sip-nueng', 'sip-ed')
out = sign + out

if d != '' :
    out = out + '-jood'
    for c in d:
        k = int(c)*5
        out = out + "-" + th[k:k+5].strip()
        
print(out)
