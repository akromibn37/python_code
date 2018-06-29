class Card:
	def __init__(self, value, suit):
		self.value = value
		self.suit = suit
	def __str__(self):
		return "(" + str(self.value) + " " + str(self.suit) + ")"
	def getScore(self):
		if self.value in 'JQK':
			return '10'
		elif self.value == 'A':
			return '1'
		else:
			return str(self.value)
	def sum(self, other):
		s = int(self.getScore()) + int(other.getScore())
		if s==20:
			return '0'
		elif s>=10:
			return str(s-10)
		else:
			return str(s)
	def __lt__(self, rhs):
		s = '34567890JQKA2'
		su = ['club','diamond','heart','spade']
		sp = s.find(self.value)
		if sp == -1: sp = 7
		op = s.find(rhs.value)
		if op == -1: op = 7
		#print("sp,op :",sp,op)
		if sp == op:
			ss = su.index(self.suit)
			os = su.index(rhs.suit)
			#print("ss,os :",ss,os)
			return ss<os
		else:
			return sp<op
		
n = int(input())
cards = []
for i in range(n):
	value, suit = input().split()
	cards.append(Card(value, suit))
for i in range(n):
	print(cards[i].getScore())
print("----------")
for i in range(n-1):
	print(Card.sum(cards[i], cards[i+1]))
print("----------")
cards.sort()
for i in range(n):
	print(cards[i])