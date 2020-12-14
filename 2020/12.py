# cLx 2020 day 12

import math

def sind(deg):
	return math.sin(math.radians(deg))

def cosd(deg):
	return math.cos(math.radians(deg))

def solve1(filename):
	x = 0; y = 0; a = 0

	fd = open(filename)
	for line in fd:
		line = line.strip()
		op = line[0]
		arg = int(line[1:])

		if   op == 'N': y+=arg
		elif op == 'S': y-=arg
		elif op == 'E': x+=arg
		elif op == 'W': x-=arg
		elif op == 'L': a+=arg
		elif op == 'R': a-=arg
		elif op == 'F':
			y+= int(sind(a)) * arg
			x+= int(cosd(a)) * arg

	distance = abs(x)+abs(y)
	print(filename, "manhattan distance (part 1):", distance)
	return distance

def rotate(xw, yw, arg):
	s, c = int(sind(arg)), int(cosd(arg))
	return c*xw - s*yw, s*xw + c*yw

def solve2(filename, xw=10, yw=1):
	xb = 0; yb = 0
	s = {'L': 1, 'R':-1}

	fd = open(filename)
	for line in fd:
		line = line.strip()
		op = line[0]; arg = int(line[1:])

		if   op == 'N': yw+=arg
		elif op == 'S': yw-=arg
		elif op == 'E': xw+=arg
		elif op == 'W': xw-=arg
		elif op == 'L' or op == 'R':
			xw, yw = rotate(xw, yw, s[op]*arg)
		elif op == 'F':
			xb+=xw*arg; yb+=yw*arg

	distance = abs(xb)+abs(yb)
	print(filename, "manhattan distance (part 2):", distance)
	return distance

# part 1
assert solve1("input/12.input.test") == 25
assert solve1("input/12.input") == 319

# part 2
assert solve2("input/12.input.test") == 286
assert solve2("input/12.input") == 50157
