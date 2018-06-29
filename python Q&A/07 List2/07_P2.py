zero2z = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
inp = list(input())
counts = [inp.count(e) for e in zero2z]
print(" ".join([str(e) for e in counts]))
