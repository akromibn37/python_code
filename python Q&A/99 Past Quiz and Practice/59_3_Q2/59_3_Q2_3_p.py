dna = input().strip().upper()
for c in dna:
    if c not in 'ATGC':
        print('Invalid DNA')
        exit(0)

op = input().strip()

if op == 'R':
    ans = ''
    for c in dna:
        if c == 'A': ans = 'T'+ans
        if c == 'T': ans = 'A'+ans
        if c == 'G': ans = 'C'+ans
        if c == 'C': ans = 'G'+ans
    print(ans)

elif op == 'F':
    a = t = g = c = 0
    for k in dna:
        if k == 'A': a += 1
        if k == 'T': t += 1
        if k == 'G': g += 1
        if k == 'C': c += 1
    print('A='+str(a)+', T='+str(t)+', G='+str(g)+', C='+str(c))

elif op == 'D':
    p = input().strip()
    ans = 0
    for i in range(len(dna)-1):
        if dna[i:i+2] == p:
            ans += 1
    print(ans)
