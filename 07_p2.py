l = [0] * 62
c = input().strip()
num = "0123456789"
low = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ans = ""
for i in c:
	if i in num:
		k = num.index(i)
		l[k] +=1
	elif i in low:
		k = low.index(i)
		l[k+36] +=1
	elif i in upper:
		k = upper.index(i)
		l[k+10] +=1
for j in range(len(l)):
	ans += str(l[j]) + " "
print(ans)