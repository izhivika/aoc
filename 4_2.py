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
d = {}
q = 0
for i in range(len(b)):
    if b[i][3] != 'f' and b[i][3] != 'w':
        if b[i][3] not in d:
            d[b[i][3]] = q
            q += 1
c = [[0 for j in range(60)] for i in range(len(d))]
for i in range(len(b)):
    if b[i][3] in d:
        for j in range(i+1, len(b)):
            if b[j][3] == 'f':
                x_f = b[j][2]
            elif b[j][3] == 'w':
                x_w = b[j][2]
                for k in range(x_f, x_w):
                    c[d[b[i][3]]][k] += 1
            else:
                break
days = 0
for i in range(len(c)):
    for j in range(60):
        if c[i][j] > days:
            days = c[i][j]
            minute = j
            the_value = i
for key, value in d.items():
	if value == the_value:
		the_id = key
		break
print(the_id*minute)