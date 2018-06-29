infile = open("score.txt")
sid = input().strip()
for line in infile:
    id,g = line.split()
    if sid == id :
        print(g)
        break
else:
    print("Not Found")
infile.close()
