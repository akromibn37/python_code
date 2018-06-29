books = list()
fin = open('books.txt')
for line in fin:
    x = [e.strip() for e in line.split(',')]
    books.append([x[0],set(x[1:])])
fin.close()
q = {e.strip() for e in input().split(',')}
c = 0
for b in books:
    if q.issubset(b[1]) :
        print(b[0])
        c += 1
if c == 0: print('Not found')
