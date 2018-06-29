def eq_or_neq(x,y,z):
    return x==y==z or (x!=y and y!=z and x!=z)

def isSet(c1,c2,c3):
    for i in range(4):
        if not eq_or_neq(c1[i],c2[i],c3[i]):
            return False
    return True

cards = []
for i in range(12):
    cards.append(input().strip().split())
for i in range(12):
    for j in range(i+1,12):
        for k in range(j+1,12):
            if isSet(cards[i],cards[j],cards[k]):
                print(i,j,k)
