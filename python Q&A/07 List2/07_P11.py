a,b = [int(e) for e in input().split()]
for i in range(a):
    g = 0
    n = 0
    x = [e for e in input().strip().split()]
    for i in range(b):
        if x[i]=="A":
            g+=4 
        elif x[i]=="B+":
            g+=3.5
        elif x[i]=="B":
            g+=3
        elif x[i]=="C+":
            g+=2.5
        elif x[i]=="C":
            g+=2
        elif x[i]=="D+":
            g+=1.5
        elif x[i]=="D":
            g+=1
        elif x[i]=="F":
            g+=0
        else:
            n-=1           
        n+=1
    print("{:.2f}".format(g/n))
            
        

