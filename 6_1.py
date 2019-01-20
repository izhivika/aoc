import string
with open('6_input.txt', 'r') as inp:
	a = []
	for line in inp:
		s = line.strip()
		a += [s]
b = [[0 for j in range(2)] for i in range(len(a))]
w = ''
for i in range(len(a)):
	for j in range(2):
		w += a[i][j]
	if a[i][2] != ',':
		w += a[i][2]
	b[i][0] = int(w)
	w = ''
	for j in range(-1, -3, -1):
		w = a[i][j] + w
	if a[i][-3] != ' ':
		w = a[i][-3] + w
	b[i][1] = int(w)
	w = ''
x_max = 0
y_max = 0
for i in range(len(b)):
	if b[i][0] > x_max:
		x_max = b[i][0]
	if b[i][1] > y_max:
		y_max = b[i][1]
c = [[0 for j in range(x_max+1)] for i in range(y_max+1)]
for i in range(len(b)):
	if i < 26:
		c[b[i][1]][b[i][0]] = 'A' + string.ascii_uppercase[i]
	else:
		c[b[i][1]][b[i][0]] = 'B' + string.ascii_uppercase[i-26]
