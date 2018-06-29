n1 = float(input())
s =0
i=0
while n1!=-1:
	i+=1
	s+=n1
	n1 = float(input())	
if i==0:	
	print("No Data")
else:
	print(s/i)
	