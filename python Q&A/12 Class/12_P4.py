class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return "("+self.value+" "+self.suit+")"

    def next1(self):
        if self.suit == "club":
            return Card(self.value,"diamond")
        if self.suit == "diamond":
            return Card(self.value,"heart")
        if self.suit == "heart":
            return Card(self.value,"spade")
        if self.value == "A":
            return Card("2","club")
        if self.value == "J":
            return Card("Q","club")
        if self.value == "Q":
            return Card("K","club")
        if self.value == "K":
            return Card("A","club")
        if self.value == "10":
            return Card("J","club")
        return Card(str(int(self.value)+1),"club")

    def next2(self):
        n = self.next1()
        self.value = n.value
        self.suit = n.suit

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