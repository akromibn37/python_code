names = dict()
n = 0
while True:
    x = input().split()
    if len(x)==1 and x[0] == 'end' : break
    n += 1
    singer = x[0]
    if singer not in names: names[singer] = (n,list())
    for e in x[1:]:
        if e not in names[singer][1]:
            names[singer][1].append(e)

for k in range(len(names.keys())) :
    _, _, singer = min([ (len(names[s][1]),names[s][0],s) for s in names])
    choose = names[singer][1][0]
    print(singer,choose)
    names.pop(singer)
    for s in names:
        if choose in names[s][1] : names[s][1].remove(choose)

    
             
          
    


