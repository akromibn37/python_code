import math
m = input().strip()
w = float(input().strip())
c = 0
if m == "E":
	if w>0 and w<=10000:
		if w>9500:
			c = 487
		elif w>9000:
			c = 457
		elif w>8500:
			c = 427
		elif w>8000:
			c = 397
		elif w>7500:
			c = 367
		elif w>7000:
			c = 342
		elif w>6500:
			c = 317
		elif w>6000:
			c = 292
		elif w>5500:
			c = 267
		elif w>5000:
			c = 242
		elif w>4500:
			c = 217
		elif w>4000:
			c = 197
		elif w>3500:
			c = 177
		elif w>3000:
			c = 157
		elif w>2500:
			c = 137
		elif w>2000:
			c = 122
		elif w>1500:
			c = 97
		elif w>1000:
			c = 82
		elif w>500:
			c = 67
		elif w>250:
			c = 52
		elif w>100:
			c = 42
		elif w>20:
			c = 37
		else :
			c = 32	
		print(c)
	else:
		print("ERROR")

elif m == "N":
	co =0
	if w>11000:
		i = w-11000
		co = math.ceil(i/1000)
		x = w-i
	else:
		x = w
	if x > 0 :
		if x>10000:
			c = 170
		elif x>9000:
			c = 155 
		elif x>8000:
			c = 140
		elif x>7000:
			c = 125	
		elif x>6000:
			c = 110 
		elif x>5000:
			c = 95
		elif x>4000:
			c = 80	
		elif x>3000:
			c = 65 
		elif x>2000:
			c = 50
		elif x>1000:
			c = 35	
		else :
			c = 20	
		print(c+(co*15))
	else:
		print("ERROR")
	
elif m == "R":
	if w>0 and w<=2000 :
		if w>1000:
			c = 58
		elif w>500:
			c = 38
		elif w>250:
			c = 28
		elif w>100:
			c = 22		
		else :
			c = 18	
		print(c)
	else:
		print("ERROR")

