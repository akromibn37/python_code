num = "0123456789"
inp = list(input())
counts = [inp.count(e) for e in num]
print("\n".join([str(e) for e in counts]))
