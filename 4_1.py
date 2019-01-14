with open('4_input.txt', 'r') as inp:
	a = []
	for line in inp:
		s = line.strip()
		a += [s]
b = [[0 for j in range(4)] for i in range(len(a))]
for i in range(len(a)):
	date = ''
	for j in range(1, 11):
		date += a[i][j]
	b[i][0] = date
	if int(a[i][12]+a[i][13]) == 0:
		b[i][1] = 24
	else:
		b[i][1] = int(a[i][12]+a[i][13])
	b[i][2] = int(a[i][15]+a[i][16])
	if a[i][19] == 'G':
		q = a[i][26]
		for j in range(3):
			if a[i][27+j] != ' ':
				q += a[i][27+j]
			else:
				break
		b[i][3] = int(q)
	else:
		b[i][3] = a[i][19]
b.sort()
#with open('4_1_output.txt', 'w') as out:
#	for i in range(len(b)):
#		out.write(str(b[i]) + '\n')
d = {}
for i in range(len(b)):
	if b[i][3] != 'f' and b[i][3] != 'w':
		x = 0
		for j in range(i+1, len(b)):
			if b[j][3] == 'f':
				x_f = b[j][2]
			elif b[j][3] == 'w':
				x_w = b[j][2]
				x += x_w - x_f
			else:
				break				
		if b[i][3] not in d:
			d[b[i][3]] = x
		else:
			x_new = d[b[i][3]] + x
			d[b[i][3]] = x_new
max_minutes = 0
for value in d.values():
	if value > max_minutes:
		max_minutes = value
for key, value in d.items():
	if value == max_minutes:
		max_id = key
		break
c = [0 for i in range(60)]
for i in range(len(b)):
	if b[i][3] == max_id:
		for j in range(i+1, len(b)):
			if b[j][3] == 'f':
				x_f = b[j][2]
			elif b[j][3] == 'w':
				x_w = b[j][2]
				for k in range(x_f, x_w):
					c[k] += 1
			else:
				break
days = 0
for i in range(len(c)):
	if c[i] > days:
		days = c[i]
		minute = i
print(max_id*minute)		