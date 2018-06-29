def int_to_roman(x):
	roman = ["I","V","X","L","C","D","M"]
	number = [1,5,10,50,100,500,1000]
	s = ""
	val = x
	while val>0:
		if val >= 1000:
			val-=1000
			s+="M"
		elif val >= 900:
			val-= 900
			s+= "CM"
		elif val >= 500:
			val-= 500
			s+= "D"
		elif val >= 400:
			val-= 400
			s+= "CD"
		elif val>= 100:
			val-=100
			s+= "C"
		elif val>=90:
			val-=90
			s+= "XC"
		elif val>=50:
			val-=50
			s+= "L"
		elif val >=40:
			val-=40
			s+= "XL"
		elif val>=10:
			val-=10
			s+="X"
		elif val>=9:
			val-=9
			s+="IX"
		elif val>=5:
			val-=5
			s+= "V"
		elif val>=4:
			val-=4
			s+= "IV"
		else:
			val-=1
			s+="I"
	return s
def roman_to_int(x):
	roman = ["I","V","X","L","C","D","M"]
	number = [1,5,10,50,100,500,1000]
	roman_minus = ["IV","IX","XL","XC","CD","CM"]
	number_minus = [-2,-2,-20,-20,-200,-200]
	s = 0
	minus = 0
	for i in range(len(x)):
		s+= number[roman.index(x[i])]
	#print(s)
	for i in range(len(roman_minus)):
		if roman_minus[i] in x:
			minus += number_minus[i]
	s = s+minus
	#print(s)
	return s
class roman :
	def __init__(self, r):
		self.r = r
	def __lt__(self, rhs):
		return int(self)<int(rhs)
	def __str__(self):
		'''if  str(self.r).isnumeric():
			s = int_to_roman(self.r)
			return s'''				
		return self.r
	def __int__(self):
		return roman_to_int(self.r)
	def __add__(self, rhs):
		return roman(int_to_roman(int(self)+int(rhs)))	
t, r1, r2 = input().split()
a = roman(r1); b = roman(r2)
if t == '1' : print(a < b)
elif t == '2' : print(int(a),int(b))
elif t == '3' : print(str(a),str(b))
elif t == '4' : print(int(a + b))
else : print(str(a + b))
