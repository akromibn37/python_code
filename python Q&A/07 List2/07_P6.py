n = int(input())
d = [0]*n
for i in range(n):
    d[i] = int(input())
#---------------------------
s = 0
for e in d:
    s += e
mean = s/n
#---------------------------
d.sort()
median = (d[(n-1)//2] + d[n//2])/2
#---------------------------
mode = 0
maxcount = 0
for i in range(n):
    count = 0
    for j in range(i,n):
        if d[i] == d[j]:
            count += 1
    if count > maxcount:
        maxcount = count
        mode = d[i]
#---------------------------
print(mean,median,mode)
        
        
    
