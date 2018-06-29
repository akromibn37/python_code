t = input().strip()
a,b = [int(e) for e in input().split()]
if a == 0:
    print(t[b::-1] + t[b+1:])
else:
    print(t[:a] + t[b:a-1:-1] + t[b+1:])

# print(t[:a] + t[a:b+1][::-1] + t[b+1:])
