infile = open("score.txt")
data = [line.split() for line in infile]
infile.close()
ids = [id for id,score in data]
ids.sort(reverse=True)
for id in ids:
    print(id)