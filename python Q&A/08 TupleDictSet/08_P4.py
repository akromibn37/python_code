x = [int(e) for e in input().split()]
K = int(input())
n = len(x)
a = [1 for i in range(n) for j in range(i+1,n) if x[i]+x[j]==K]    
print(len(a))
