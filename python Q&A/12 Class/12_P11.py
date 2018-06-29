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

def int_to_roman(x):
  a = x//1000
  b = x//100%10
  c = x//10%10
  d = x%10

  out = ''
  if a==1: out += 'M'
  if a==2: out += 'MM'
  if a==3: out += 'MMM'
  if a==4: out += 'MMMM'
  
  if b==1: out += 'C'
  if b==2: out += 'CC'
  if b==3: out += 'CCC'
  if b==4: out += 'DC'
  if b==5: out += 'D'
  if b==6: out += 'DC'
  if b==7: out += 'DCC'
  if b==8: out += 'DCCC'
  if b==9: out += 'CM'
  
  if c==1: out += 'X'
  if c==2: out += 'XX'
  if c==3: out += 'XXX'
  if c==4: out += 'LX'
  if c==5: out += 'L'
  if c==6: out += 'LX'
  if c==7: out += 'LXX'
  if c==8: out += 'LXXX'
  if c==9: out += 'XC'
  
  if d==1: out += 'I'
  if d==2: out += 'II'
  if d==3: out += 'III'
  if d==4: out += 'IV'
  if d==5: out += 'V'
  if d==6: out += 'VI'
  if d==7: out += 'VII'
  if d==8: out += 'VIII'
  if d==9: out += 'IX'
  
  return out

class roman :
 def __init__(self, r):
  self.r = r

 def __lt__(self, rhs):
  return int(self) < int(rhs)

 def __str__(self):
  return self.r

 def __int__(self):
  return roman_to_int(self.r)

 def __add__(self, rhs):
   return roman(int_to_roman(int(self)+int(rhs)))
   
t, r1, r2 = input().split()
a = roman(r1); b = roman(r2)
if t == '1' : print(a < b)
elif t == '2' : print(int(a),int(b))
elif t == '3' : print(str(a),str(b))
elif t == '4' : print(int(a + b))
else : print(str(a + b))