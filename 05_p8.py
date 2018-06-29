f = input().strip()
fn = open(f,'r')
c = fn.readline().strip()
w = fn.readline().strip()
cw = len(w)
if c == 'find':
	for line in fn:
		wo,s,e = line.strip().split(" ")
		p = wo.find(w,int(s),int(e))
		if p != -1 :
			if p == 0:
				print(wo[:p+cw+1])
			else:
				print(wo[p-1:p+cw+1])
		else :
			print("not found")
elif c == 'rfind':
	for line in fn:
		wo,s,e = line.strip().split(" ")
		p = wo.rfind(w,int(s),int(e))
		if p != -1 :
			if p == 0:
				print(wo[:p+cw+1])
			else:
				print(wo[p-1:p+cw+1])
		else :
			print("not found")
		