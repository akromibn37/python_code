def KS(i,w,v,x):
  if i < 0 : return 0
  if x < w[i] :
    return KS(i-1,w,v,x)
  else:
    k1 = KS(i-1,w,v,x)
    k2 = KS(i-1,w,v,x-w[i])+v[i]
    return max(k1,k2)

w = [int(e) for e in input().split()]
v = [int(e) for e in input().split()]
W = int(input())
print(KS(len(w)-1,w,v,W))
