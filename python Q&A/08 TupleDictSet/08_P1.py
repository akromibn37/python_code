n = int(input())
id2cities = dict()
ids = list()
for i in range(n):
  uid,cities = input().split(":")
  id2cities[uid] = {e.strip() for e in cities.split(",")}
  ids.append(uid)
  
keyid  = input().strip()
cities = id2cities[keyid]
out = [uid for uid in ids
       if uid != keyid and len(cities & id2cities[uid]) > 0]

if len(out) == 0:
    print("Not Found")
else:
    print('\n'.join(out))
