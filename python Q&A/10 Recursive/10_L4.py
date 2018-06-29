def copylist(x):
    if type(x) is list :
        return [copylist(e) for e in x]
    return x

exec(input().strip())
