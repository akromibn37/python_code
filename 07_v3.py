infile = open("hotels.txt", "r")
hotels = []
for line in infile:
	[hotel, stars, review] = line.split(";")
	hotels.append([hotel, int(stars), float(review)])
infile.close()
#print(hotels)
star = int(input())
found_hotels = []
for h in hotels:
	if h[1] >= star:
		found_hotels.append(h)
		#print(h[0], h[1], h[2])
if len(found_hotels) == 0:
	print("Not Found")
else:
	for i in range(len(found_hotels)-1):
		for j in range(len(found_hotels)-1):
			if found_hotels[j][2]< found_hotels[j+1][2]:
				found_hotels[j],found_hotels[j+1] = found_hotels[j+1],found_hotels[j]
for h in found_hotels:
	print(h[0], h[1], h[2])
		