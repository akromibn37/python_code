fin = open('address.txt')
addr = dict()
for line in fin:
    fn,ln,t = line.split()
    addr[(fn,ln)] = t
fin.close()
while True:
    x = input().split()
    if len(x) == 0 : break
    elif len(x) == 2 :
        k = (x[0],x[1])
        if k not in addr :
            print('Not Found')
        else:
            print(addr[k])
    elif len(x) == 1 :
        for k in addr.keys():
            if addr[k] == x[0]:
                print(k[0],k[1])
                break
        else:
            print('Not Found')
