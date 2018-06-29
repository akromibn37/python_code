f = open("circulations.txt",'r')
data=[]
for line in f:
	[bookid, memberid, date] = line.split()
	data.append([bookid, memberid, int(date)])	
f.close()
#print(data)
due = int(input().strip())
found_data = []
for i in data:
	if due-i[2]>0:
		found_data.append(i)
if len(found_data) == 0:
	print("Not Found")
else:
	for i in range(len(found_data)-1):
		for j in range(len(found_data)-1):
			if found_data[j][2]> found_data[j+1][2]:
				found_data[j],found_data[j+1] = found_data[j+1],found_data[j]
for h in found_data:
	print(h[0], h[1], h[2])