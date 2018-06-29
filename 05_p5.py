f1 = input().strip()
f2 = input().strip()
fn1 = open(f1,'r')
fn2 = open(f2,'r')
for i,j in zip(fn1,fn2):
	if j.strip() in i.strip() :
		print("True")
	else :
		print("False")	
		
