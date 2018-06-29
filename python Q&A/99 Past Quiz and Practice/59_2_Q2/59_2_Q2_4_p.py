filename=input().strip()
line_num=int(input())
fi=open(filename,'r')
t0=''
t1=''
t2=''
t3=''
out=''
found=False
for line in fi:
    # print(line)
    t,m,s=line.strip().split(';')
    t3,t2,t1=t2,t1,t0
    t0=m+';'+s
    if s.lower()=='failure':
        if len(t3) != 0 and line_num == 3:
            out += t3+'\n'
        if len(t2) != 0 and line_num >= 2:
            out += t2+'\n'
        if len(t1) != 0 and line_num >= 1:
            out += t1+'\n'
        out += t0
        found=True
        break
if not found:
    out = "Not Found"
print(out)
