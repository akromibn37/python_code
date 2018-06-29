s = {int(e) for e in input().split()}
K = int(input())
a = [1 for e in s if e < K-e and K-e in s ]
print(len(a))
