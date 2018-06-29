s       = input().strip()
rot_str = 'abcdefghijklmnopqrstuvwxyzabcdefghijkl'
rot_str = rot_str+rot_str.upper()+'01234567890123456789'
count   = 0
out     = ''
offset  = -1
c_num   = -1
for c in s:
    if offset == -1:
        offset = int(c)
    elif c_num == -1:
        c_num = int(c)
    else:
        count += 1
        if c not in rot_str:
            out += c
        else:
            ind = rot_str.find(c) 
            out += rot_str[ind+offset]
        if count == c_num:
            count  = 0
            offset = -1
            c_num  = -1
print(out)

