a = input().strip()
b = input().strip()
if a in b :
    print('SUBSTRING')
else:
    isSUBSEQ = True
    p = 0
    for e in a:
        k = b.find(e,p)
        if k == -1:
            isSUBSEQ = False
            break
        p = k+1
    if isSUBSEQ :
        print('SUBSEQUENCE')
    else:
        print('NONE')
