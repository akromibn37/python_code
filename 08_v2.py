f1 = open("file1.txt")
sa = set()
for line in f1:
    line = line.replace('"', ' ') \
                  .replace('"', ' ') \
                  .replace("-", ' ') \
                  .replace(".", ' ') \
                  .replace("(", ' ') \
                  .replace(")", ' ') \
                  .replace(",", ' ')
    sa.update(line.lower().split())
print(sa)
f2 = open("file2.txt")
sb = set()
for line in f2:
    line = line.replace('"', ' ') \
                  .replace('"', ' ') \
                  .replace("-", ' ') \
                  .replace(".", ' ') \
                  .replace("(", ' ') \
                  .replace(")", ' ') \
                  .replace(",", ' ')
    sb.update(line.lower().split())
print(sb)
w = input().strip()
if w in (sa&sb):
    print('Found in both files')
elif w in sa:
    print('Found in file1 only')
elif w in sb:
    print('Found in file2 only')
else:
    print('Not found')