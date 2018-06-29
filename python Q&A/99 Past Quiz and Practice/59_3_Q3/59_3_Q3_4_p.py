import math

qt = []
q = list() # ลิสต์ q ใช้เก็บข้อมูลบัตรคิวที่เหมาะสม
n = int(input()) # อ่านจานวนคาสั่ง
for k in range(n):
    c = input().split() # อ่านข้อมูลคาสั่ง
    if c[0] == 'reset':
        next_queue = int(c[1])

    elif c[0] == 'new':
        print('ticket',next_queue)
        q.append([next_queue,int(c[1])])
        next_queue += 1

    elif c[0] == 'next':
        next_order = q[0]
        q = q[1:]
        print('call',next_order[0])

    elif c[0] == 'order':
        t = int(c[1])-next_order[1]
        print('qtime',next_order[0],t)
        qt += [t]

    elif c[0] == 'avg_qtime':
        print('avg_qtime',sum(qt)/len(qt))