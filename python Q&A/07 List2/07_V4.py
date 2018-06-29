d = input().strip()
fin = open('circulations.txt')
out = []
for line in fin:
    bid,mid,due = line.split()
    if d > due:
        out.append([due,mid,bid])
if len(out) == 0:
    print('Not Found')
else:
    out.sort()
    for due,mid,bid in out:
        print(' '.join([bid,mid,due]))
