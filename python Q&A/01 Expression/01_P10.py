s = input().strip()
n = int(s)
n9 = n % 10; n //= 10
n8 = n % 10; n //= 10
n7 = n % 10; n //= 10
n6 = n % 10; n //= 10
n5 = n % 10; n //= 10
n4 = n % 10; n //= 10
n3 = n % 10; n //= 10
n2 = n % 10; n //= 10
n1 = n % 10; n //= 10
n10 = (11-(10*n1+9*n2+8*n3+7*n4+6*n5+5*n6+4*n7+3*n8+2*n9)%11)%11
print(s+str(n10))
