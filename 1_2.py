a = []
s = 0
b = set()
w = False
with open('1_input.txt', 'r') as inp:
	for line in inp:
		a += [int(line.strip())]
while w == False:
	for i in range(len(a)):
		s += a[i]
		if s not in b:
			b.add(s)
			print(s, end=' ')
		else:
			w = True
			print()
			print('the answer:', s)
			break 