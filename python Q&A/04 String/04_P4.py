date = input().strip()
m = int(date[0:2])
d = int(date[3:5])
y = int(date[6:10])
day2month = 'JANFEBMARAPRMAYJUNJULAUGSEPOCTNOVDEC'
print(d,day2month[3*m-3:3*m],y)
