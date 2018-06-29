w2words = dict()
for i in range(int(input())):
  _, w = input().split()
  w2 = w[:2]
  if w2 not in w2words: w2words [w2] = []
  w2words[w2].append(w)
  
nmax,w2max = min([(-len(w2words[w2]),w2) for w2 in w2words])
print(w2max)
print(-nmax)
print('\n'.join(w2words[w2max]))
