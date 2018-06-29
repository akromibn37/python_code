def distance(p,q):
 return ( (p[0]-q[0])**2 + (p[1]-q[1])**2 )**0.5
 
def perimeter(points):
  p = list(points + points[0:1])
  return sum([ distance(p[i],p[i+1]) for i in range(len(p)-1)])

s = input().strip().split()
p = [(float(t[1:t.find(',')]),float(t[t.find(',')+1:-1])) for t in s]
print(perimeter(p))
