class piggybank:
 def __init__(self):
   self.coins = dict()
 def add(self, v, n):
   if sum(self.coins.values()) + n > 100 : return False
   v = float(v)
   if v not in self.coins : self.coins[v] = 0
   self.coins[v] += n
   return True
 def __float__(self):
   s = 0.0
   for v in self.coins:
     s += self.coins[v]*v
   return s
 def __str__(self):
   x = []
   for v in sorted(self.coins.keys()):
     x.append(str(v)+":"+str(self.coins[v]))
   return "{" + ", ".join(x) + "}"
     
cmd1 = input().split(';')
cmd2 = input().split(';')
p1 = piggybank(); p2 = piggybank()
for c in cmd1: eval(c)
for c in cmd2: eval(c)
