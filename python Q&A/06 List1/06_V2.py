f = open(input().strip())
s = []
for line in f:
  sid,fname,lname,ms,fs = line.split(";")
  sc = float(ms) + float(fs)
  if sc >= 80 : g = 'A'
  elif sc >= 70 : g = 'B'
  elif sc >= 60 : g = 'C'
  elif sc >= 50 : g = 'D'
  else: g = 'F'
  s.append([sid, fname+' '+lname, g])
f.close()
print(s)
