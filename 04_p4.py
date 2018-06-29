w = input()
m,d,y = w.split("/")
if m == "01":
	m = "JAN"
elif m=="02":
	m = "FEB"
elif m == "03":
	m = "MAR"
elif m=="04":
	m = "APR"
elif m=="05":
	m = "MAY"
elif m == "06":
	m = "JUN"
elif m=="07":
	m = "JUL"
elif m=="08":
	m = "AUG"
elif m == "09":
	m = "SEP"
elif m=="10":
	m = "OCT"
elif m == "11":
	m = "NOV"
elif m=="12":
	m = "DEC"
print(d,m,y)
