info = dict()
for k in range(int(input())):
    a_student = input().split()
    info[a_student[0]] = a_student[1:]
    
query = set(input().split())
result = [name for name in info.keys()
            if query.issubset(info[name]) ]

if len(result)==0:
    print('Not Found')
else:
    for name in sorted(result):
        print(name,' '.join(info[name]))
