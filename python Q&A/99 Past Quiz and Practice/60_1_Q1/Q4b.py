result = input().strip()       # ?? case in the 10th frame
target = int(input())
i = 0
total = 0
for f in range(1,11):
    if result[i:i+3] == 'XXX' :     # XXX   -> 30
        sc = 30
        i += 1
    elif result[i:i+2] == 'XX' :    # XX?   -> 20 + ?
        sc = 20 + int(result[i+2])
        i += 1
    elif result[i:i+3:2] == 'X/' :  # X?/   -> 20
        sc = 20
        i += 1
    elif result[i] == 'X' :         # X??   -> 10 + ? + ?
        sc = 10 + int(result[i+1]) + int(result[i+2])
        i += 1
    elif result[i+1:i+3] == '/X' :  # ?/X   -> 20
        sc = 20
        i += 2
    elif result[i+1] == '/':        # ?/?   -> 10 + ?
        sc = 10 + int(result[i+2])
        i += 2
    else :                          # ??    -> ? + ?
        sc = int(result[i]) + int(result[i+1])
        i += 2

    total += sc
    if f == target :
        print(total)
        break
else:
    print(total)
