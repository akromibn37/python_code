s = input().strip()
inf = open(s)
for line in inf:
    line = line.strip()
    id, s1,s2,s3,s4,s5 = line.split()
    suma = int(s1) + int(s2) + int(s3) + int(s4) +int(s5)
    if suma >= 80 :
        grade = "A"
    elif suma >= 75 :
        grade = "B+"
    elif suma >= 70 :
        grade = "B"
    elif suma >= 65 :
        grade = "C+"
    elif suma >= 60 :
        grade = "C"
    elif suma >= 55 :
        grade = "D+"
    elif suma >= 50 :
        grade = "D"
    else :
        grade = "F"
    print(id,grade)
inf.close()
