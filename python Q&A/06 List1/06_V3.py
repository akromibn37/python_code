f = open(input().strip())
s = []
ids = []
for line in f:
  line = line.strip()
  if line == '' : continue
  sid,fname,lname,ms,fs = line.split(";")
  if sid in ids : continue
  ids.append(sid)
  sc = float(ms) + float(fs)
  if sc >= 80 : g = 'A'
  elif sc >= 70 : g = 'B'
  elif sc >= 60 : g = 'C'
  elif sc >= 50 : g = 'D'
  else: g = 'F'
  s.append([sid, fname+' '+lname, g])
f.close()
sid = input().strip()
while sid != '-1' :
  if sid not in ids :
    print('Not Found')
  else:
    k = ids.index(sid)
    print(s[k])
  sid = input().strip()
