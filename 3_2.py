with open('3_input.txt', 'r') as inp:
	data = []
	for line in inp:
		s = line.strip().split()
		del s[0]
		del s[0]
		s[0] = s[0].split(',')
		s[0][1] = s[0][1].replace(':','')
		s[1] = s[1].split('x')
		data += [s]
for i in range(len(data)):
	for j in 0,1:
		for k in 0,1:
			data[i][j][k] = int(data[i][j][k])
max_x_s = 0
max_width = 0
max_y_s = 0
max_height = 0
for i in range(len(data)):
	if data[i][0][0] > max_x_s:
		max_x_s = data[i][0][0]
	if data[i][0][1] > max_y_s:
		max_y_s = data[i][0][1]
	if data[i][1][0] > max_width:
		max_width = data[i][1][0]
	if data[i][1][1] > max_height:
		max_height = data[i][1][1]
max_x_f = max_x_s + max_width
max_y_f = max_y_s + max_height
a = [[0 for j in range(max_x_f)] for i in range(max_y_f)]
for i in range(len(data)):
	for j in range(data[i][0][0], (data[i][0][0] + data[i][1][0])):
		for k in range(data[i][0][1], (data[i][0][1] + data[i][1][1])):
			a[j][k] += 1
sum = 0
for i in range(len(data)):
	for j in range(data[i][0][0], (data[i][0][0] + data[i][1][0])):
		for k in range(data[i][0][1], (data[i][0][1] + data[i][1][1])):
			sum += a[j][k]
	if sum == data[i][1][0] * data[i][1][1]:
		print(i+1)
		break
	sum = 0