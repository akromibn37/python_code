class Complex :
	def __init__(self,a,b):
		self.re = a
		self.im = b
	def __str__(self):
		if self.re == 0 and self.im == 0:
			return "0"
		elif self.re == 0:
			if self.im > 0:
				if self.im == 1:
					return "i"
				else:
					return str(self.im) + "i"
			else:
				if self.im == -1:
					return "-i"
				else:
					return str(self.im) + "i"
		elif self.im == 0:
			return str(self.re)
		else:
			if self.im>0:
				if self.im ==1:
					return str(self.re) + "+i"
				else:
					return str(self.re) + "+" + str(self.im) + "i"  
			else :
				if self.im ==-1:
					return str(self.re) + "-i"
				else:
					return str(self.re) + str(self.im) + "i"  
	def __add__(self,rhs):
		real = self.re + rhs.re
		image = self.im + rhs.im
		return Complex(real,image)
	def __mul__(self,rhs):
		real = (self.re*rhs.re) - (self.im*rhs.im)
		image = (self.re*rhs.im) + (self.im*rhs.re)		
		return Complex(real,image)
	def __truediv__(self,rhs):
		d = (rhs.re**2 + rhs.im**2)
		real = ((self.re*rhs.re) + (self.im*rhs.im))/d
		image = float((-(self.re*rhs.im) + (self.im*rhs.re))/d)
		#print(real,image)
		return Complex(real,image)
t, a, b, c, d = [int(x) for x in input().split()]
c1 = Complex(a,b)
c2 = Complex(c,d)
if t == 1 : print(c1)
elif t == 2 : print(c2)
elif t == 3 : print(c1+c2)
elif t == 4 : print(c1*c2)
else : print(c1/c2)