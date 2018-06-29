filename = input().strip()
f = open(filename)
code = f.readline().strip()
pattern = f.readline().strip()
if code == "T2M":
	for line in f:
		line = line.strip()
		morse = ""
		check = True
		txt = ""
		for e in line:
			j = pattern.rfind(']' + e + '[',0,len(pattern))
			k = pattern.rfind('[',0,j)
			morse += pattern[k+1:j] + ' '
			txt+=e
			if j == -1:
				check = False
		if check == True:print(morse.strip())
		else: print("Invalid :",txt)
elif code == "M2T":
	for line in f:
		line = line.strip()
		mos = line.split(" ")
		txt = ""
		check = True
		morse = ""
		for i in range(len(mos)):
			morse += mos[i] + ' '
			j = pattern.find("["+mos[i]+"]")			
			if j==-1:
				check = False
			txt += pattern[j+len(mos[i])+2:j+len(mos[i])+3]
		if check == True: print(txt)
		else: print("Invalid :",morse)
else:
	print("Invalid code")
f.close()