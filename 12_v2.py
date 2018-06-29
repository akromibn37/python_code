import math
class Circle:
	def __init__(self,index,x,y,r):
		self.index = index
		self.x = x
		self.y = y
		self.r = r
	def touch(self,other):
		if distance(self.x,self.y,other.x,other.y) < (self.r+other.r):
			return 'Overlap'
		elif distance(self.x,self.y,other.x,other.y) == (self.r+other.r):
			return 'Touch'
		return 'Free'
def distance(x1,y1,x2,y2): # หาระยะห่างระหว่างจุดสองจุด
	return ((x1-x2)**2+(y1-y2)**2)**0.5
 # ส่วนของโปรแกรมหลัก
n = int(input().strip())
circles = []
for i in range(n):
	circle_input = [int(e) for e in input().strip().split()]
	circle = Circle(circle_input[0],circle_input[1],circle_input[2],circle_input[3])
	circles.append(circle)
	#print(circles[i].index)
output = []
# วน loop เช็ควงกลมทุกวง ส่วนนี้ให้เขียนเอง ถ้าเจอวงกลมที่ Free ให้เอามาเก็บใน output
for i in range(n):
	for j in range(n):
		if i!=j and circles[i].touch(circles[j]) != 'Free': break
	else:
		output.append(circles[i].index)
		
if len(output) == 0:
	print('Not Found')
else:
	print(' '.join([str(e) for e in output]))
