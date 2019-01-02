with open('2_input.txt') as inp:
	x = 0
	two = 0
	three = 0
	twocheck = False
	threecheck = False
	y = set()
	for line in inp:
		s = line.strip()
		for i in range(len(s)):
			if s[i] not in y:
				y.add(s[i])
				for j in range(len(s)):
					if s[j] == s[i]:
						x += 1
				if x == 2 and twocheck == False:
					two += 1
					twocheck = True
				elif x == 3 and threecheck == False:
					three += 1
					threecheck == True
			x = 0
		twocheck = False
		threecheck = False
		y.clear()
checksum = two * three
print(checksum) 
		