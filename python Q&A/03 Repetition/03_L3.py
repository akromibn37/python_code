n,b = [int(e) for e in input().split()]
if b < 2 or b > 9 :
    print("Error: Cannot convert")
else:
    out = ""
    while n > 0:
        out = str(n%b) + out
        n //= b
    if out == "":
        print(0)
    else:
        print(out)
