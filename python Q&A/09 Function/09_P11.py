def zscore(L):
 mean = sum(L)/len(L)
 sd = (sum([(e-mean)**2 for e in L])/len(L))**0.5
 return [(e-mean)/sd for e in L]
 
L = [float(e) for e in input().split()]
for i in zscore(L): 
 print(i)
