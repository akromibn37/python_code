def eat(q1,q2):
  return q1[0]==q2[0] or q1[1]==q2[1] or \
         abs(q1[0]-q2[0])==abs(q1[1]-q2[1])
  
def all_eat(L):
  return sorted([(i,j) for i in range(len(L))
                        for j in range(i+1,len(L))
                          if eat(L[i],L[j])])
  
print(eval(input().strip()))
