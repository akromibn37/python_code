n = int(input())
out = ''
if n > 0 : out += 'positive '
elif n < 0 : out += 'negative '
else : out += 'zero '
if n%2 == 0 : out += 'even'
else : out += 'odd'
print(out)
