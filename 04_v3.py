'''t = ' '+input().strip().lower()+' '
p = ' '+input().strip().lower()+' '
t = t.replace('"',' ')
t = t.replace("'",' ')
t = t.replace(',',' ')
t = t.replace('.',' ')
print(t)
print(p)

if p in t:
    print("Found")
else:
    print("Not Found")

'''
s = ' ' +input().lower()+' '
w = ' ' +input().lower()+' '
output = ""

for c in s:
	if c in " \" ' , . ( )" :
		output += " "
	else :
		output += c

if w in output:
		print("Found")
else :
	print("Not Found")