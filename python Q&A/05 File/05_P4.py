infile = open(input().strip())
be = se = ve = et = 0
for line in infile:
    code,desc = line.split()
    code = code.lower()
    if code == 'be': be += 1
    if code == 'se': se += 1
    if code == 've': ve += 1
    if code == 'et': et += 1
infile.close()        
print(be,se,ve,et,be+se+ve+et)
