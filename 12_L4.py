class piggybank:
	def __init__(self):
		 # มีตัวแปร self.coins เก็บ dict เริ่มต้นให้ว่าง ๆ
		 # มี key เป็นมูลค่าเหรียญ และ value เป็นจ านวนเหรียญ
		self.coins = dict()
	def add(self, v, n):
		 # ถ้าเพิ่มจ านวนเหรียญในกระปุกอีก n เหรียญแล้วเกิน 100
		 # จะไม่ให้เพิ่ม ให้คืน False แทนว่า เพิ่มไม่ส าเร็จ
		 # แปลง v เป็น float ก่อน (เพิ่ม 5 กับ 5.0 จะได้เหมือนกัน)
		 # ถ้ากระปุกไม่เคยมีเหรียญ v ท า self.coins[v]= 0
		 # ท าค าสั่ง self.coins[v] += n
		 # คืน True แทนว่าเพิ่มส าเร็จ
		if sum(self.coins.values()) + n > 100: return False
		else:
			v = float(v)
			if v not in self.coins:
				self.coins[v] = n
			else:
				self.coins[v] += n
		return True
	 
	def __float__(self):
		 # น าค่าของเหรียญคูณกับจ านวนเหรียญ ของเหรียญทุกแบบ
		 # ต้องคืนจ านวนแบบ float เท่านั้น อยากคืนศูนย์ ก็ต้อง 0.0
		s = 0.0
		for v in self.coins:
			#print(v)
			s+=self.coins[v]*v
		return s
	def __str__(self):
		 # คืนสตริงที่แสดงจ านวนเหรียญแต่ละแบบตามตัวอย่าง
		 # โดยให้เรียงเหรียญตามมูลค่าจากน้อยไปมาก
		out = ""
		for i in sorted(self.coins):
			out += str(i) + ":" + str(self.coins[i]) + ", "
		out = out[:-2]
		#print(out)
		return "{" + out + "}"
		#out = "{"
		#for i in range(len(self.coins)):
		#	out += self.coins[i].keys + ":" +self.coins[i].values + ", "
		#out = out[:-2]
		#print(out)
		#return out
cmd1 = input().split(';')
cmd2 = input().split(';')
p1 = piggybank(); p2 = piggybank()
for c in cmd1: eval(c)
for c in cmd2: eval(c)
