avail = dict()
for k in range(int(input())):
    d, n = input().split()
    avail[d] = int(n)
    
students = list()
for k in range(int(input())):
    sid, p, d1, d2, d3, d4 = input().split()
    students.append((float(p),sid,(d1,d2,d3,d4)))

students.sort(reverse=True)
out = []
for p,sid,choices in students: 
    for dept in choices:
        if avail[dept] > 0:
            out.append((sid,dept))
            avail[dept] -= 1
            break
        
out.sort()
for k in range(len(out)):
    print(' '.join(out[k]))
