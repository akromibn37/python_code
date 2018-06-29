import math

d = float(input())
if d < 0 : print("ERROR"); exit(0)
f = 0.0
if d > 0 : f += 35
if 1 < d : f += math.ceil(min(d-1,9))*5.5
if 10 < d : f += math.ceil(min(d-10, 10))*6.5
if 20 < d : f += math.ceil(min(d-20, 20))*7.5
if 40 < d : f += math.ceil(min(d-40, 20))*8.0
if 60 < d : f += math.ceil(min(d-60, 20))*9.0
if 80 < d : f += math.ceil(d-80)*10.5
print(f)
