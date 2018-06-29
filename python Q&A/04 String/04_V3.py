t = ' '+input().strip().lower()+' '
p = ' '+input().strip().lower()+' '
t = t.replace('"',' ')
t = t.replace("'",' ')
t = t.replace(',',' ')
t = t.replace('.',' ')

if p in t:
    print("Found")
else:
    print("Not Found")
