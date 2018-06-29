def read_data():
    # read data from keyboard, add the data into dict D
    # and return dict D when done
    D = dict()
    n = int(input()) # number of student's records to read in
    for k in range(n):
        sid,name,gpax,year,dept = [e.strip() for e in input().strip().split(',')]
        gpax = float(gpax); year = int(year)
        if dept not in D:
            D[dept] = {sid:(name,gpax,year)}
        else:
            D[dept][sid] = (name,gpax,year)
    return D

def is_in(D, sid, dept):
    # return True if sid is in dept, otherwise return False
    return dept in D and sid in D[dept] 

def get_year(D, sid):
    # return the year of sid
    # if sid does not exist, return False
    for dept in D:
      if sid in D[dept]:
        return D[dept][sid][2]
    return False

def get_supers(D, dept):
    # return a set of sids in dept that have year greater than 4
    # if dept does not exist, return False
    # note that an empty set is returned if no supers in the existing dept.
    if dept not in D:
      return False
    s = set()
    for sid in D[dept]:
      if D[dept][sid][2] > 4:
        s.add(sid)
    return s

def max_gpax(D):
    # return max gpax among all students in D
    mx = -1
    for dept in D:
      for sid in D[dept]:
        mx = max(mx,D[dept][sid][1])
    return mx

def get_max_gpax_students(D):
    # return a set of tuples of students' sid and name 
    # who got the max gpax among all students in D
    mx = max_gpax(D)
    s = set()
    for dept in D:
      for sid in D[dept]:
        if D[dept][sid][1] == mx:
          s.add((sid,D[dept][sid][0]))
    return s
   
# do not remove the following lines!!
n = int(input())              
for k in range(n):
    exec(input().strip())
