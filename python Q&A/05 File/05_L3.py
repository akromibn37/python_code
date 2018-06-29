f = open(input().strip())
c_sum = 0
for line in f:
    for c in line:
        c_sum = c_sum ^ ord(c)
f.close()
print(c_sum)
