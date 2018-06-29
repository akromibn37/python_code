class Card:	
	def __init__(self, value, suit):
		self.value = value
		self.suit = suit
	def __str__(self):
		return "(" + str(self.value) + " " + str(self.suit) + ")"
	def next1(self):
		s = '34567890JQKA2'
		su = ['club','diamond','heart','spade']
		p1 = s.find(self.value)
		p2 = su.index(self.suit)
		v = ""
		i = ""
		if p1 == -1: p1 = 7
		if p2 == 3:
			p2 = 0
			if p1 == 12: 
				p1 = 0
				v = s[p1];i=su[p2]
				if v == '0' : v = "10"
			else:
				v = s[p1+1];i=su[p2]
				if v == '0' : v = "10"
		else:
				v = s[p1];i=su[p2+1]
				if v == '0' : v = "10"

		return Card(v,i)				
	def next2(self):
		s = '34567890JQKA2'
		su = ['club','diamond','heart','spade']
		p1 = s.find(self.value)
		p2 = su.index(self.suit)
		v = ""
		i = ""
		if p1 == -1: p1 = 7
		if p2 == 3:
			p2 = 0
			if p1 == 12: 
				p1 = 0
				self.value = s[p1];self.suit=su[p2]
				if self.value == '0' : self.value = "10"
			else:
				self.value = s[p1+1];self.suit=su[p2]
				if self.value == '0' : self.value = "10"
		else:
				self.value = s[p1];self.suit=su[p2+1]		
				if self.value == '0' : self.value = "10"

n = int(input())
cards = []
for i in range(n):
	value, suit = input().split()
	cards.append(Card(value, suit))
for i in range(n):
	print(cards[i].next1())
print("----------")
for i in range(n):
	print(cards[i])
print("----------")
for i in range(n):
	cards[i].next2()
	cards[i].next2()
	print(cards[i])