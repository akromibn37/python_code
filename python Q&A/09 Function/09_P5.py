def roman_to_int(string):
  table=[['M',1000],['CM',900],['D',500],['CD',400],['C',100],['XC',90],\
         ['L',50],['XL',40],['X',10],['IX',9],['V',5],['IV',4],['I',1]]
  returnint=0
  for pair in table:
    check=True
    while check:
      if len(string)>=len(pair[0]):
        if string[0:len(pair[0])]==pair[0]:
          returnint+=pair[1]
          string=string[len(pair[0]):]
        else: check=False
      else: check=False
  return returnint
  
n = int(input())
d = []
for i in range(n):
  s = input()
  d.append((roman_to_int(s),s))
d.sort()
for (m,s) in d:
  print(s)
