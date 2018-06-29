n = input()
out = ""
if n.find("0") == -1:
	out+= "0 "
if n.find("1") == -1:
	out+= "1 "
if n.find("2") == -1:
	out+= "2 "
if n.find("3") == -1:
	out+= "3 "
if n.find("4") == -1:
	out+= "4 "
if n.find("5") == -1:
	out+= "5 "
if n.find("6") == -1:
	out+= "6 "
if n.find("7") == -1:
	out+= "7 "
if n.find("8") == -1:
	out+= "8 "
if n.find("9") == -1:
	out+= "9 "
if out=="":
	print("No missing digits")
else:
	print(out)