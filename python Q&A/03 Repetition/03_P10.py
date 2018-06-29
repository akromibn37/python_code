n = int(input())
out = ""
for k in range(n-1,1,-1):
    if n%k == 0:
        out += str(k)+" "
if out == "":
    print("Prime Number")
else:
    print(out.strip())
