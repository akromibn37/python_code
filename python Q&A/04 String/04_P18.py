n = int(input())
a = input().strip()
b = input().strip()
npre = npos = 0
for i in range(npre+1,len(a)+1):
  if a[:i] == b[:i] :
    npre = i
for i in range(npos+1,len(a)+1):
  if a[-i:] == b[-i:] :
    npos = i
for k in range(2,n):
    a = a[:npre]
    b = b[-npos:]
    c = input().strip()
    npre = npos = 0
    for i in range(npre+1,len(a)+1):
      if a[:i] == c[:i] :
        npre = i
    for i in range(npos+1,len(b)+1):
      if c[-i:] == b[-i:] :
        npos = i    
if npre == 0:
    print("NO COMMON PREFIX")
else:
    print(a[:npre])
if npos == 0:
    print("NO COMMON SUFFIX")
else:
    print(b[-npos:])
