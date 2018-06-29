fin = open('cards.txt')
n = int(input())
while n > 0:
  line = fin.readline().strip()
  n -= 1
fin.close()

c = 'A234567890JQK'
out = 'Y'
for i in range(len(line)-1):
  if c.find(line[i]) > c.find(line[i+1]) : out = 'N'
print(out)
