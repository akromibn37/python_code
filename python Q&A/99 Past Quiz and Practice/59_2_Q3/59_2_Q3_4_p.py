n = int(input())
dic = {}
for i in range(n) :
    x = input().strip().split(',')
    if x[0] not in dic.keys() :
        dic[x[0]] = set([x[1]])
    else :
        if x[1] not in dic.values() :
            dic[x[0]].add(x[1])
cid = {}
for j in dic :
    for k in dic[j] :
        if k not in cid.keys() :
            cid[k] = 1
        else :
            cid[k] += 1
lis = []
for z in cid :
    lis.append((z,cid[z]))
for y in range(len(lis)-1) :
    for x in range(len(lis)-1) :
        if lis[x][1] < lis[x+1][1] :
            lis[x],lis[x+1] = lis[x+1],lis[x]
for y in range(len(lis)-1) :
    for x in range(len(lis)-1) :
        if lis[x][1] == lis[x+1][1] and lis[x][0] > lis[x+1][0] :
            lis[x],lis[x+1] = lis[x+1],lis[x]
ris = []
for u in range(3) :
    ris.append(lis[u][0])
print(','.join(ris))


