infile = open("data.txt",'r')
n = input()
sum = 0
count = 0
for line in infile:
	sid,name,sec,score = line.split(":")
	if sec == n :
		sum += float(score)
		count += 1
		
if count==0 :
	print("Not Found")
else :
	print(sum/count)