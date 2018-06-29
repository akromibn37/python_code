class test1:
	def __init__(self,x,y)
		self.x=x;self.y=y
	def	add(self,x,y)
		return x+y
	def	sub(self,x,y)
		return x-y
	def	print(self,x,y)
		return 'x = ' + x + ' y = ' + y;

t1=test1(3,2)
add = t1.add
sub = t1.sub
print(add)
print(sub)
text = t1.print
print(text)
		