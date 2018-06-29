n = int(input())
sum = 0
for i in range(n):
	n1 = float(input())
	sum+=n1
if n == 0:
	print("No Data")
else:
	print(sum/n)