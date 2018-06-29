def C(n,k):
  if k == 0 or n == k : return 1
  if k < 0 or k > n : return 0
  return C(n-1,k)+C(n-1,k-1)

n = int(input())
k = int(input())
print(C(n,k))
