s = open('5_input.txt').read().strip()
def react(polymer):
	i = 1
	while i < len(polymer):
		a = polymer[i-1]
		b = polymer[i]		
		if a != b and a.upper() == b.upper():
			del polymer[i-1:i+1]
			if i > 1: i = i - 1
		else: i = i + 1
	return polymer

reacted = react(list(s))

print("Star 1:", len(reacted))

from string import ascii_lowercase
print("Star 2:", min(len(react([x for x in reacted if x.lower() != c])) for c in  ascii_lowercase))