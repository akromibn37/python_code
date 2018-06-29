min = 100000
max = 0
i = 0
while i<6 :
	a = int(input())
	if max < a :
		max = a
	if min > a :
		min = a
	i = i + 1
print(min,max)