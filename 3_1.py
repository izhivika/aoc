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
width = 0
height = 0
area = 0
check = False
for i in range(len(x)):
	x_s_i = data[i][0][0]
	x_f_i = x_s_i + data[i][1][0]
	y_s_i = data[i][0][1]
	y_f_i = y_s_i + data[i][1][1]
	x_s_j = data[j][0][0]
	x_f_j = x_s_j + data[j][1][0]
	y_s_j = data[j][0][1]
	y_f_j = y_s_j + data[j][1][1]
	if check == False:
		for j in range(len(x)):
			if 
print(data)