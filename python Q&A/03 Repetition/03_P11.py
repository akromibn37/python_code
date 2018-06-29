n = int(input())
if n < 0 :
    print("input unavailable")
else:
    out = ""
    for m in range(2,n+1):
        is_prime = True
        for k in range(2,int(m**0.5)+1):
            if m%k == 0:
                is_prime = False
                break
        if is_prime :
            out += str(m) + " "
    if out == "":
        print("none")
    else:
        print(out)
