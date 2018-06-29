word = input().strip()
w1,w2 = word.split()
w1o=""
w2o=0
for i in range(len(w1)):
	if i==0:
		w1o+=w1[i].upper()
	else:
		w1o+=w1[i].lower()
for i in w2:
	if i in "0123456789":
		w2o+= int(i)
print(w1o,w2o)
		