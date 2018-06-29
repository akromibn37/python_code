f = open("data.txt")
s = input().strip()
n = 0
sum = 0
for line in f:
    id,name,sec,sc = line.strip().split(":")
    if sec == s:
        sum += float(sc)
        n += 1
f.close()
if n > 0:
    print(sum/n)
else:
    print("Not Found")
