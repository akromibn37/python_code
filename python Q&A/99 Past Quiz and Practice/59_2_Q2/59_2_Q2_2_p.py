x = int(input())

# for output, if x is negative, begin with '-'
if x < 0:
    temp = -x
    output = '-'
else:
    temp = x
    output = ''

# find out how many digit and maximum divider
digit = 1
divider = 1

while temp > 0:
    temp = temp//10
    if temp > 0:
        digit += 1
        divider *= 10

temp = abs(x)
for i in range(digit):
    k = temp // divider % 10
    temp = temp%divider

    if k != 0:
        output += str(k) + '*' + str(divider)
        # not last digit
        if temp > 0:
            if x < 0:
                output += ' - '
            else:
                output += ' + '

    divider = divider // 10

# special case when x is 0(zero)
if x == 0:
    output += '0'
    
print(x, '=', output)
