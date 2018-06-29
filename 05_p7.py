f = input().strip()
fn = open(f,'r')
sum = 0
for line in fn:
	if line.strip() == "" :
		sum+=1
print(sum)