def B_to_A(b):
    if len(b) == 1 and type(b[0]) is int :
        return [[b[0]]]
    if type(b[0]) is int :
        return [ [b[0]]+e for e in B_to_A(b[1])]
    else :
        return [e for p in b for e in B_to_A(p)]
    
print(B_to_A(eval(input().strip())))
