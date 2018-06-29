infile = open("score.txt")
data = [line.split() for line in infile]
infile.close()
while True:
    sid = input().strip()
    if sid == "-1" : break
    for id,g in data:
        if sid == id :
            print(g)
            break
    else:
        print("Not Found")
