import math
class Circle:
    def __init__(self,sid,x,y,r,color):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.sid = sid
    def area(self):
        return math.pi*self.r**2
    
    def contain_point(self,px,py):
        # ทดสอบว่าจุดอยู่ในวงกลมหรือไม่ ถ้าอยู่จะคืน True ถ้าไม่อยู่ จะคืน False
        if distance(self.x,self.y,px,py) <= self.r:
            return True
        return False
    def touch(self,other):
        # ทดสอบว่าวงกลมสองวง ซ้อนทับกัน หรือว่า แตะกัน หรือไม่
        d = distance(self.x,self.y,other.x,other.y)
        if d < self.r + other.r :
            return 'Overlap'
        elif d == self.r + other.r:
            return 'Touch'
        return 'Free'
def distance(x1,y1,x2,y2):
    # หาระยะห่างระหว่างจุดสองจุด
    return ((x1-x2)**2+(y1-y2)**2)**0.5


n = int(input())
px,py = [float(e) for e in input().split()]
circles = []
for k in range(n):
    x,y,r,c = [float(e) for e in input().split()]
    circles.append(Circle(k,x,y,r,c))

cids = [{e} for e in range(n)]
for i in range(n):
    for j in range(i+1,n):
        if circles[i].touch(circles[j])!='Free': 
            if circles[i].sid != circles[j].sid :
                for cid in cids[circles[j].sid]:
                    circles[cid].sid = circles[i].sid
                    cids[circles[i].sid].add(cid)
                    cids[cid] = set()

for k in range(n):
    if circles[k].contain_point(px,py):
        sumc = 0; sumarea = 0 
        for cid in cids[circles[k].sid]:
            sumarea += circles[cid].area()
            sumc += circles[cid].area()*circles[cid].color
        print(sumc/sumarea)
        break
else:
    print(1.0)
