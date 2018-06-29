class rint:
	def __init__(self,r):
		out = ""
		for i in range(len(r)-1,-1,-1):
			out+=r[i]
		print(out)
		self.r = out
	def __lt__(self,rhs):
		return int(self)<int(rhs)
	
	def __str__(self):
		return self.r
	
	def __int__(self):
		return int(self.r[::-1])
	
	def __add__(self,rhs):
		c = int(self) + int(rhs)
		return rint(str(c)[::-1])
		
t, r1, r2 = input().split()
a = rint(r1); b = rint(r2)
if t == '1' : print(a < b)
elif t == '2' : print(int(a),int(b))
elif t == '3' : print(str(a),str(b))
elif t == '4' : print(int(a + b))
else : print(str(a + b))