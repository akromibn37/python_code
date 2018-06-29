w1,w2 = input().split()
sum = 0    
for c in w2:
    if "0" <= c <= "9" : sum += int(c)
print(w1[0].upper() + w1[1:].lower(), sum)
