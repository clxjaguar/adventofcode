# cLx 2021 day 2

def solve1(filename):
	fd = open(filename, 'r')
	x = 0; z = 0
	for line in fd:
		d, n = line.split()
		n = int(n)
		if d == "up":
			z-=n
		elif d == "down":
			z+=n
		elif d == "forward":
			x+=n
	return(x* z)

def solve2(filename):
	fd = open(filename, 'r')
	x = 0; a = 0; z = 0
	for line in fd:
		d, n = line.split()
		n = int(n)
		if d == "up":
			a-=n
		elif d == "down":
			a+=n
		elif d == "forward":
			x+=n
			z+=(a*n)
	return(x* z)

assert solve1('input/2.input.test') == 150
assert solve1('input/2.input') == 1499229

assert solve2('input/2.input.test') == 900
assert solve2('input/2.input') == 1340836560
