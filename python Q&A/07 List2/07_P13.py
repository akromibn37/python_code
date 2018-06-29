x = int(input())
y = int(input())
L = []
for i in range (x) :
  L.append(input().split())
for i in range (x) :
  for j in range(x) :
    if L[i] == L[j] and i<j :
      print(i+1)
      print(" ".join(L[i]))
      print(j+1)
      print(" ".join(L[j]))

