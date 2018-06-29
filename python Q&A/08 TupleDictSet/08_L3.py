import string
filename = input().strip()
file = open(filename, "r")
word = file.read()
word = word.split()
count = dict()
for w in word :
    w = w.strip(string.punctuation + string.whitespace)
    w = w.lower()
    count[w] = count.get(w, 0) + 1
d = [(-count[c],c) for c in count]
d.sort()
d = [(e,-c) for c,e in d]
print(d[0:10])
file.close()