class piggybank:
	def __init__(self):
	# มีตัวแปร 4 ตัวเก็บจ านวนเหรียญของเหรียญแต่ละแบบ
		self.c1 = 0
		self.c2 = 0
		self.c5 = 0
		self.c10 = 0
	def add1(self, n):
	# เพิ่ม n ในตัวแปรที่เก็บจ านวนเหรียญบาท
		self.c1+=n
	def add2(self, n):
	# เพิ่ม n ในตัวแปรที่เก็บจ านวนเหรียญสองบาท
		self.c2+=n
	def add5(self, n):
	# เพิ่ม n ในตัวแปรที่เก็บจ านวนเหรียญห้าบาท
		self.c5+=n
	def add10(self, n):
	# เพิ่ม n ในตัวแปรที่เก็บจ านวนเหรียญสิบบาท
		self.c10+=n
	def __int__(self):
	# คืนมูลค่ารวม = ค่าของเหรียญคูณกับจ านวนเหรียญ
		return (self.c1*1)+(self.c2*2)+(self.c5*5)+(self.c10*10)
	def __lt__(self, rhs):
	# เปรียบเทียบจ านวนเงินใน self กับจ านวนเงินใน rhs
		return int(self)<int(rhs)
	def __str__(self):
	# คืนสตริงที่แสดงจ านวนเหรียญแต่ละแบบตามตัวอย่าง
		#st = "{1:" + self.c1 + ", ", "2:" + self.c2 + ",","5:" + self.c5 + ",", "10:" + self.c10 + "}"
		st = "{1:" + str(self.c1) + ", " +  "2:" + str(self.c2) + ", " + "5:" + str(self.c5) + ", "+ "10:" + str(self.c10) + "}"
		return st
cmd1 = input().split(';')
cmd2 = input().split(';')
p1 = piggybank(); p2 = piggybank()
for c in cmd1: eval(c)
for c in cmd2: eval(c)