n = int(input())
result = 0
i = 0
while n > 0:
    k = n % 10
    d = 2**i
    result += k*d
    n //= 10
    i = i+1
print(result)
