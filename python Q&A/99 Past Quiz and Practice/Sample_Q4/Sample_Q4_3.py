def remove_symbol(s):
  symbol = '0123456789+-,./!'
  out = ''
  for c in s:
    if c in symbol: out += ' '
    else: out += c.lower()
  return out
  
def str_to_unique_list(s):
  s = remove_symbol(s)
  out = []
  for e in s.split():
      if e.strip() not in out:
          out.append(e.strip())
  return out
  
def percent_in_list(template, test):
  count = 0
  for w in test:
      if w in template: count += 1
  return count*100/len(test)
 
def main():
 good = input().strip()
 good_list = str_to_unique_list(good)
 bad = input().strip()
 bad_list = str_to_unique_list(bad)
 n = int(input())
 for i in range(n):
   test = input().strip()
   test_list = str_to_unique_list(test)
   good_p = percent_in_list(good_list, test_list)
   bad_p = percent_in_list(bad_list, test_list)
   print(test_list)
   print(good_p, bad_p)

exec(input().strip())
# do not remove this line
