filename = input()
a = int(input())
b = input()
c = input()
f = open(filename,'r')
i = 1
for line in f :
	text = line
	if i<=a:
		text = text.replace(b,c,a)
		i+=1
	print(text)

		
	