courses = dict()
fc = open(input().strip())
for line in fc:
    cid,name = [e.strip() for e in line.split(',')]
    courses[cid] = name
fc.close()

teachers = dict()
ft = open(input().strip())
for line in ft:
    tid,name = [e.strip() for e in line.split(',')]
    teachers[tid] = name
ft.close()

fd = open(input().strip())
for line in fd:
    cid,tid = [e.strip() for e in line.split(',')]
    if cid not in courses or tid not in teachers:
        print('record error')
    else:
        print(courses[cid]+','+teachers[tid])
fd.close()
