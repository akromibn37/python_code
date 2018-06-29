import math

x = float(input())
k = 0
cosine = 0
term = 0
while True:
    term = ((-1)**k * (x**(2*k)))/math.factorial(2*k)
    if abs(term) < 1e-8:
        break
    cosine += term
    k += 1

print(cosine,k-1)
