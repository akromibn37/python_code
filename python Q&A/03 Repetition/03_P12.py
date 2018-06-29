n = int(input())
out = ""
k = 2
while k <= n:
    if n%k == 0 :
        out += str(k) + " "
        while n%k == 0:
            n //= k
    k += 1
print(out)
