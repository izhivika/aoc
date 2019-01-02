with open('1_input.txt', 'r') as inp:
	s = 0
	for line in inp:
		s += int(line.strip())
print(s)