import math
ih = int(input())
im = int(input())
oh = int(input())
om = int(input())
i = ih*60 + im
o = oh*60 + om
r = o-i
p = 0
if r <= 15:
	p = 0
elif r<=180 :
	p=math.ceil(r/60)*10
elif r<=360 :
	x = r-180
	p = 30+ (math.ceil(x/60)*20)
else:
	p = 200
print(p)