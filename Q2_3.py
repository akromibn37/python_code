n = int(input().strip())
f = open("cards.txt",'r')
j = 1
c = True
for line in f:
	if j==n:
		for i in range(len(line)-2):
			if line[i] =='A':
				x = '1'
			elif line[i] == 'J':
				x = '11'
			elif line[i] == 'Q':
				x = '12'
			elif line[i] == 'K':
				x = '13'
			elif line[i] == '0':
				x = '10'
			else:
				x = line[i]
				
			if line[i+1] =='A':
				y = '1'
			elif line[i+1] == 'J':
				y = '11'
			elif line[i+1] == 'Q':
				y = '12'
			elif line[i+1] == 'K':
				y = '13'
			elif line[i+1] == '0':
				y = '10'
			else:
				y = line[i+1]
			print(x,y)
			if int(x)>int(y):
				print('N')
				c= False
				break
				
	j+=1
if c == True:
	print('Y')