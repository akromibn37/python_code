def print_money(s, m) :
    sorted_m = sorted([ (v, m[v]) for v in m ])
    sorted_m = sorted_m[::-1] # reverse order --> max to min
    print(s,','.join([str(v)+":"+str(c) for v,c in sorted_m if c>0]))
#---------------------------------------------
money = input().strip().split(",")
pocket_money = dict()
for item in money :
    v, c = [int(e) for e in item.split(":")]
    pocket_money[v] = c

print_money("In pocket:", pocket_money)
#---------------------------------------------
# compute total amount of money in the pocket
pocket_amount = 0
for i in pocket_money:
    pocket_amount += i*pocket_money[i]

#---------------------------------------------
pay_amount = int(input())
if pay_amount > pocket_amount :
    print("Not enough money")
else :
    pay_money = dict()
    sorted_money = sorted([ (v, pocket_money[v]) for v in pocket_money ])
    sorted_money = sorted_money[::-1] # reverse order --> max to min
    p = pay_amount
    for value,count in sorted_money :
        if value*count > p:
            c = p // value
        else :
            c = count
        p -= value*c
        pay_money[value] = c
    if p != 0 :
        print("Not match")
    else :
        print_money("Pay:", pay_money)
        #-------------------------------------
        # update pocket_money after changing
        for i in pocket_money:
            pocket_money[i] -= pay_money[i]

        #-------------------------------------
        print_money("Left in pocket:", pocket_money)
