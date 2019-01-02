with open('2_input.txt') as inp:
	x = []
	for line in inp:
		s = line.strip()
		x += [s]
w = 0
for i in range(len(x)):
	for j in range(len(x)):
		for k in range(len(x[i])):
			if (x[j])[k] == (x[i])[k]:
				w += 1
		if w == 25:
			print()
			print('the answer is:')
			print(x[i])
			print(x[j])
			break
		w = 0