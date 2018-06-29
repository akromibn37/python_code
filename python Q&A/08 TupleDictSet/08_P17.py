winners = set()
losers = set()
for k in range(int(input())):
    w,l = input().split()
    losers.add(l)
    if w not in losers : winners.add(w)
    if l in winners : winners.remove(l)

print(sorted(winners))
