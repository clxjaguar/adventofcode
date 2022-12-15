# cLx 2022 day 14

def sgn(v):
	if v>0: return 1
	if v<0: return -1
	return 0

def printField(field, xmin, xmax, ymin, ymax):
	for y in range(0, ymax+3):
		line = ['.' if y<=ymax+1 else '='] * ((xmax - xmin) + 1)
		if y==0:
			line[500-xmin] = '+'
		for x in range(xmin, xmax+1):
			if (x, y) in field:
				line[x-xmin] = field[(x, y)]
		print("%3d %s" % (y, ''.join(line)))
	print()

from itertools import count

def solve(filename, assertPart1=None, assertPart2=None):
	fd = open(filename, 'r')

	field = {}
	for line in fd:
		coords = [tuple(map(int, item.split(','))) for item in line.strip().split(' -> ')]
		x, y = coords[0]
		field[(x, y)] = '#'
		for xTarget, yTarget in coords[1:]:
			while x != xTarget or y != yTarget:
				x+=sgn(xTarget-x); y+=sgn(yTarget-y)
				field[(x, y)] = '#'

	xmax, ymax = max([x for x, y in field]), max([y for x, y in field])
	xmin, ymin = min([x for x, y in field]), min([y for x, y in field])

	printField(field, xmin, xmax, min(ymin, 0), ymax)

	part1 = None; part2 = None
	for i in count(1):
		x = 500; y = 0
		while y < ymax+1:
			# ~ print(x, y)
			if (x, y+1) not in field:
				y+=1
			elif (x-1, y+1) not in field:
				y+=1; x-=1
			elif (x+1, y+1) not in field:
				y+=1; x+=1
			else:
				field[(x, y)] = 'o'
				break
		else:
			if part1 == None: part1 = i-1
			field[(x, y)] = 'o'
			if x<xmin: xmin=x
			if x>xmax: xmax=x

		# ~ print("Iteration", i)

		if y == 0:
			part2 = i
			break

	printField(field, xmin, xmax, min(ymin, 0), ymax)

	print("%s (part 1): %d" % (filename, part1))
	if assertPart1 != None:
		assert part1 == assertPart1

	print("%s (part 2): %d" % (filename, part2))
	if assertPart2 != None:
		assert part2 == assertPart2

solve('input/14.input.test', assertPart1=24,  assertPart2=93)
solve('input/14.input',      assertPart1=799, assertPart2=29076)
solve('input/14.input2',     assertPart1=892, assertPart2=27155)
