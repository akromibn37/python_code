def function1():
    sum = 0
    for i in range(10):
        sum += i
    return sum

def function2(n):
    i = 2
    if n == 1:
        return False
    while i <= n**0.5:
        if n%i == 0:
            return False
        i += 1
    return True

def function3(n):
    for i in range(1,n):
        if function2(i):
            print(i)

def function4(x,y):
    match = 0
    notmatch = ''
    for i in x:
        if i == y:
            match += 1
        else:
            notmatch += i
    return [match,notmatch]


fn = input().strip()
if fn == 'function1' :
    print(function1())
elif fn == 'function2':
    a = int(input())
    print(function2(a))
elif fn == 'function3':
    a = int(input())
    function3(a)
elif fn == 'function4':
    a,b = input().split()
    print(function4(a,b))
