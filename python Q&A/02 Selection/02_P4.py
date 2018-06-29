import math

h1 = int(input())
m1 = int(input())
h2 = int(input())
m2 = int(input())
m = (h2*60+m2) - (h1*60+m1)
h = int(math.ceil(m/60))
if h > 6:
  print(200)
elif h >= 4:
  print(int(30+(h-3)*20))
elif m > 15:
  print(h*10)
else:
  print(0)
