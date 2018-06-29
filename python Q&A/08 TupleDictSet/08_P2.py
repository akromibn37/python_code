progID_to_appIDs = {}
n = int(input())
for i in range(n):
  id, p1, p2, p3, p4 = input().split(",")
  id = id.strip(); p1 = p1.strip(); p2 = p2.strip();
  p3 = p3.strip(); p4 = p4.strip();
  plist = [p1,p2,p3,p4]
  for p in plist:
      if p not in progID_to_appIDs :
        progID_to_appIDs[p] = []
      progID_to_appIDs[p].append(id)

progs = [e.strip() for e in input().split(",")]
for prog in progs:
  if prog in progID_to_appIDs :
    print(prog, "->", ", ".join(progID_to_appIDs[prog]))
  else:
    print(prog, "->", "Not found")
