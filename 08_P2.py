progID_to_appIDs = {}
n = int(input())
for i in range(n):
	id, p1, p2, p3, p4 = input().split(",")
	id = id.strip(); p1 = p1.strip(); p2 = p2.strip();
	p3 = p3.strip(); p4 = p4.strip();
	if p1 not in progID_to_appIDs:
		progID_to_appIDs[p1]=list()
	progID_to_appIDs[p1].append(id)
	if p2 not in progID_to_appIDs:
		progID_to_appIDs[p2]=list()
	progID_to_appIDs[p2].append(id)
	if p3 not in progID_to_appIDs:
		progID_to_appIDs[p3]=list()
	progID_to_appIDs[p3].append(id)
	if p4 not in progID_to_appIDs:
		progID_to_appIDs[p4]=list()
	progID_to_appIDs[p4].append(id)
print(progID_to_appIDs)	

progs = [e.strip() for e in input().split(",")]
for prog in progs:
	out = ""
	if prog in progID_to_appIDs:
		x = progID_to_appIDs[prog]
		for i in range(len(x)):
			if i==len(x)-1: out += x[i]
			else: out += x[i]+", "
		print(prog,"->",out)
	else:
		print(prog,"->","Not found")
 