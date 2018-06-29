n = int(input())
count = dict()
for k in range(n):
    events = set(input().split())
    for e1 in events:
        if e1 not in count: count[e1] = dict()
        for e2 in events:
            if e1 != e2:
                if e2 not in count[e1] : count[e1][e2] = 0
                count[e1][e2] += 1
event = input().strip()
if event not in count :
    print('Not Found')
elif len(count[event]) == 0 :
    print('No suggested event')
else:
    out = [(-count[event][e2],e2) for e2 in count[event]]
    for c,event in sorted(out):
       print(event, -c)
