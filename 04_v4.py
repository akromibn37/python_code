s = input() + " "
out = ""
num = "0123456789"
alpha = "abcdefghijklmnopqrstuvwxyz"
alphanum = alpha + alpha.upper() + num
eng = "zero one  two  threefour five six  seveneightnine "

for i in range(len(s)-1):
    if s[i] in num :
        out += eng[5*int(s[i]):5*int(s[i])+5].strip()
        if s[i+1] in alphanum :
            out += " "
    else:
        out += s[i]
print(out.strip())