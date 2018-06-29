s = input().strip()
o = ""
for c in s:
    if c in """"',.()""" :
        o += " "
    else:
        o += c
print(o)
