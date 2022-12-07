# cLx 2022 day 6

def solve(filename, dc=4):
	fd = open(filename, 'r')

	inpt = fd.readline().strip()
	for i in range(dc, len(inpt)):
		s = inpt[i-dc:i]
		if len(set(s)) == dc:
			print("%d\t%s" % (i, s))
			return i


assert solve('input/6.input.test') == 7
assert solve('input/6.input') == 1142

assert solve('input/6.input.test', 14) == 19
assert solve('input/6.input', 14) == 2803
