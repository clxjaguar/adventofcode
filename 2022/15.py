# cLx 2022 day 15

def printField(field, xmin, xmax, ymin, ymax):
	for y in range(ymin, ymax+1):
		line = ['.'] * ((xmax - xmin) + 1)
		for x in range(xmin, xmax+1):
			if (x, y) in field:
				line[x-xmin] = field[(x, y)]
		print("%3d %s" % (y, ''.join(line)))
	print()

import re

def solve(filename, assertPart1=None, assertPart2=None, debug=False):
	fd = open(filename, 'r')

	xmin, ymin, xmax, ymax, = [float('nan')]*4

	sensors = {}

	for line in fd:
		sx, sy, bx, by = map(int, re.search('Sensor at x=([-0-9]+), y=([-0-9]+): closest beacon is at x=([-0-9]+), y=([-0-9]+)', line).groups())
		r = abs(sx - bx) + abs(sy - by)
		sensors[(sx, sy)] = (r, (bx, by))
		xmin, xmax = min(sx-r, xmin), max(sx+r, xmax)
		ymin, ymax = min(sy-r, ymin), max(sy+r, ymax)
		# ~ print('sensor:', (sx, sy), 'beacon:', (bx, by), r)

	# ~ print("(%d,%d) to (%d,%d)" % (xmin, ymin, xmax, ymax))
	field = {}

	def isPositionInRangeOfAnySensor(x, y, debug=False):
		for i, sensor in enumerate(sensors):
			r, beaconCoords = sensors[sensor]
			if abs(sensor[0]-x) + abs(sensor[1]-y) <= r:
				if debug:
					field[(x, y)] = "%c" % (ord('a') + i)
				return True

		return False

	def isPositionHasNoBeacons(x, y, debug=False):
		for sensor in sensors:
			r, beaconCoords = sensors[sensor]
			if (x, y) == beaconCoords:
				return False

		return isPositionInRangeOfAnySensor(x, y, debug)

	# Part 1
	part1 = 0
	y = 10 if debug else 2000000
	for x in range(xmin, xmax+1):
		if isPositionHasNoBeacons(x, y, debug):
			part1+=1

	if debug:
		for y in range(ymin, ymax+1):
			if y == 10: continue
			for x in range(xmin, xmax+1):
				isPositionHasNoBeacons(x, y, debug)

		for sensorCoords in sensors:
			field[sensorCoords] = 'S'
			r, beaconCoords = sensors[sensorCoords]
			field[beaconCoords] = 'B'

		printField(field, xmin, xmax, ymin, ymax)

	print("%s (part 1): %d" % (filename, part1))
	if assertPart1:
		assert part1 == assertPart1

	# Part 2
	candidates = set()
	limit = 20 if debug else 4000000
	for i, a in enumerate(sensors, start=1):
		r, _ = sensors[a]
		for y in range(max(a[1]-r-1, 0), min(a[1]+r+2, limit)):
			if y < 0: exit()
			if y > limit: exit()

			dy = abs(y - a[1])
			x1 = a[0] - r + dy - 1
			x2 = a[0] + r - dy + 1

			if x1 >= 0 and x1 <= limit:
				candidates.add((x1, y))
			if x2 >= 0 and x2 <= limit:
				candidates.add((x2, y))

	if debug:
		printField(field, 0, 20, 0, 20)

	for i, c in enumerate(candidates, start=1):
		if not isPositionInRangeOfAnySensor(c[0], c[1]):
			part2 = (c[0] * 4000000) + c[1]
			print("%s (part 2): %s => %d" % (filename, c, part2))
			break

	if assertPart2:
		assert part2 == assertPart2

solve('input/15.input.test', assertPart1=26, assertPart2=56000011, debug=True)
solve('input/15.input',      assertPart1=4717631, assertPart2=13197439355220)
solve('input/15.input2',     assertPart1=5176944, assertPart2=13350458933732)
