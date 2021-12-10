# cLx 2021 day 9

import sys

def solve(filename):
	inpt = open(filename, 'r').read().strip().split()

	# load data
	heightmap = {}
	for y, line in enumerate(inpt):
		for x, char in enumerate(line):
			heightmap[(x, y)] = int(char)

	max_x, max_y = len(inpt[0]), len(inpt)
	del inpt

	# find lowest points
	heightmapLowests = {}
	for y in range(max_y):
		for x in range(max_x):
			v = heightmap[(x, y)]
			flag = True
			for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
				if (x+dx, y+dy) not in heightmap:
					continue
				if v >= heightmap[(x+dx, y+dy)]:
					flag = False
					break
			if flag:
				heightmapLowests[(x, y)] = v

	# calculate part 1 result
	result1 = 0
	for height in heightmapLowests.values():
		result1+= 1 + height
	print("%s: result of part 1 is %d" % (filename, result1))

	# now, find basins around lowest points
	basinsCoords = set()
	basinsSizes = []
	for coords, height in heightmapLowests.items():
		coordsList = []
		def exploreBasin(coords, coordsList, matchHeight):
			if coords in coordsList or coords not in heightmap:
				return

			height = heightmap[coords]
			if height >= matchHeight and height != 9:
				coordsList.append(coords)
				basinsCoords.add(coords)
				if matchHeight < 8:
					exploreBasin((coords[0]+1, coords[1]), coordsList, height+1)
					exploreBasin((coords[0]-1, coords[1]), coordsList, height+1)
					exploreBasin((coords[0], coords[1]+1), coordsList, height+1)
					exploreBasin((coords[0], coords[1]-1), coordsList, height+1)

		exploreBasin(coords, coordsList, height)
		basinsSizes.append(len(coordsList))

	# calculate part 2 result
	basinsSizes.sort(reverse=True)
	print("Basins sizes:", basinsSizes)
	result2 = basinsSizes[0] * basinsSizes[1] * basinsSizes[2]
	print("%s: result of part 2 is %d" % (filename, result2))

	# visualisation just because it's cool
	for y in range(0, max_y):
		for x in range(0, max_x):
			if (x, y) in heightmapLowests:
				sys.stdout.write("\x1B[42m\x1B[30m")
			elif (x, y) in basinsCoords:
				sys.stdout.write("\x1B[44m\x1B[97m")
			elif heightmap[(x, y)] == 9:
				sys.stdout.write("\x1B[107m\x1B[37m")
			else:
				sys.stdout.write("\x1B[41m")
			sys.stdout.write("%d" % heightmap[(x, y)])
		sys.stdout.write("\x1B[0m\n")

	return (result1, result2)

assert solve('input/9.input.test') == (15, 1134)
assert solve('input/9.input') == (591, 1113424)

