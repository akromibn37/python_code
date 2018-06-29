def sumlist(x) :
  s = 0
  for e in x :
    if type(e) is int :
      s += e
    else:
      s += sumlist(e)
  return s

print(sumlist(eval(input().strip())))
