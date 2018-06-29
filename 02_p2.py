m = float(input())
if m>=0 and m<=100 :
	if m>=80:
		g = "A"
	elif m>=75 :
		g = "B+"
	elif m>=70 :
		g = "B"
	elif m>=65 :
		g = "C+"
	elif m>=60:
		g = "C"
	elif m>=55:
		g = "D+"
	elif m>=50:
		g = "D"
	else:
		g = "F"
	print(g)
else:
	print("ERROR")
	