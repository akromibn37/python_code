likes = dict()
liked = dict()

while True:
    x = input().split()
    if x[0] == 'done':
        break
    else:
        likes[x[0]] = x[1:]
        for e in x[1:]:
            if e not in liked:
                liked[e] = set()
            liked[e].add(x[0])
x = input().split()

if x[0] == 'R':
    for k in sorted(likes.keys()):
        print(k, len(likes[k]))

elif x[0] == 'T':
    a = [(len(liked[e]),e) for e in liked]
    mx = max(a)[0]
    b = [e for (n,e) in a if n == mx]
    for e in sorted(b):
        print(e)

elif x[0] == 'C':
    a = set()
    if x[1] in liked and x[2] in liked:
        a = liked[x[1]] & liked[x[2]]
    if len(a) == 0:
        print('None')
    else:
        for e in sorted(a):
            print(e)

elif x[0] == 'M':
    a = list(set(likes.keys()) | set(liked.keys()))
    out = []
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i] in likes and a[j] in likes[a[i]] and \
               a[j] in likes and a[i] in likes[a[j]]:
                out.append((a[i],a[j]))
                out.append((a[j],a[i]))
    if len(out)==0:
      print('None')
    else:
      for e in sorted(out):
        print(e)
