f = input()
fn = open(f,'r')
be=0
se=0
ve=0
et=0
for line in fn:
	cat,item = line.strip().split()
	if cat.strip().lower() == "be":
		be+=1
	elif cat.strip().lower() == "se":
		se+=1
	elif cat.strip().lower() == "ve":
		ve+=1
	elif cat.strip().lower() == "et":
		et+=1
print(be,se,ve,et,(be+se+ve+et))		