from collections import defaultdict

next_st = defaultdict(set)
st = input().split()
while len(st) > 1 :
    next_st[st[0]].add(st[1])
    next_st[st[1]].add(st[0])
    st = input().split()
    
out = set(next_st[st[0]])
out.add(st[0])
for e in next_st[st[0]]:
    out.update(next_st[e])

print('\n'.join(sorted(list(out))))
