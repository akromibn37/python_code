fin = open('inventory.txt')
inv = [[pc,pn,int(p)] for pc,pn,p in
       [line.split(';') for line in fin]]
fin.close()
notexist = 'Product code does not exist.'
while True:
    cmd = [e for e in input().split()]
    if cmd[0] == 'T':
        for i in range(len(inv)):
            if inv[i][0] == cmd[1] :
                inv[i][2] += int(cmd[2])
                print(inv[i])
                break
        else:
            print(notexist)
    elif cmd[0] == 'U':
        for i in range(len(inv)):
            if inv[i][0] == cmd[1] :
                inv[i][2] = int(cmd[2])
                print(inv[i])
                break
        else:
            print(notexist)
    elif cmd[0] == 'A':
        for i in range(len(inv)):
            if inv[i][0] == cmd[1] :
                print('Duplicate product code.')
                break
        else:
            inv.append([cmd[1],cmd[2],int(cmd[3])])
            print(inv[-1])
    elif cmd[0] == 'D':
        for i in range(len(inv)):
            if inv[i][0] == cmd[1] :
                inv.pop(i)
                print(cmd[1],'deleted')
                break
        else:
            print(notexist)
    elif cmd[0] == 'Q':
        print('Bye!')
        break
