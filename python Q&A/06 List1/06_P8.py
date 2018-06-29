n = int(input())
a = [e for e in range(1,n+1)]
i,j = [int(e) for e in input().split()]
while (i!=0 and j!=0) :
  ii = a.index(i)
  jj = a.index(j)
  a[ii],a[jj] = a[jj],a[ii]
  i,j = [int(e) for e in input().split()]
print(a)
