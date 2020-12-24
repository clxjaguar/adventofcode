# cLx 2020 day 24

def solve(filename, assertPart1=None, assertPart2=None):
	file = open(filename).read().split()
	tiles = {}
	for line in file:
		x = 0; y = 0;
		while(len(line) > 0):
			if line.startswith("nw"):   dx = -2; dy = +3; line = line[2:]
			elif line.startswith("sw"): dx = -2; dy = -3; line = line[2:]
			elif line.startswith("se"): dx = +2; dy = -3; line = line[2:]
			elif line.startswith("ne"): dx = +2; dy = +3; line = line[2:]
			elif line.startswith("w"):  dx = -4; dy =  0; line = line[1:]
			elif line.startswith("e"):  dx = +4; dy =  0; line = line[1:]
			else:
				print("Error:", line)
				exit(-1)
			x+=dx; y+=dy;

		tile = (x, y)
		if tile not in tiles:
			tiles[tile] = True
		else:
			tiles[tile] = not tiles[tile]

	# part 1
	def countFlippedTiles(tiles):
		cnt = 0
		for tile in tiles:
			if tiles[tile] == True:
				cnt+=1
		return cnt

	ans1 = countFlippedTiles(tiles)
	print(filename, "part 1 is:", ans1)
	if assertPart1 != None:
		assert ans1 == assertPart1

	# part 2
	adjacentsLocations = ((-2, +3), (-2, -3), (+2, -3), (+2, +3), (-4,  0), (+4,  0))

	for _ in range(100):
		# make a set of the locations of all tiles of interest
		tilesToCheck = set()
		for tileCoords in tiles:
			tilesToCheck.add(tileCoords)
			for dx, dy in adjacentsLocations:
				tilesToCheck.add((tileCoords[0]+dx, tileCoords[1]+dy))

		# for each of these locations, count cells around, and update
		# a copy of our grid according to the rules
		nextTiles = tiles.copy()
		for tileCoords in tilesToCheck:
			try:
				tileState = tiles[tileCoords]
			except:
				tileState = False

			cnt = 0
			for dx, dy in adjacentsLocations:
				coords = (tileCoords[0]+dx, tileCoords[1]+dy)
				if coords in tiles and tiles[coords]:
					cnt+=1;

			if tileState == True: # black tile
				if cnt == 0 or cnt>2:
					nextTiles[tileCoords] = False

			else: # white tile
				if cnt == 2:
					nextTiles[tileCoords] = True

		# replace the grid former's state by the copy, and do it again!
		tiles = nextTiles

	ans2 = countFlippedTiles(tiles)
	print(filename, "part 2 is:", ans2)
	if assertPart2 != None:
		assert ans2 == assertPart2


solve("input/24.input.test", assertPart1=10,  assertPart2=2208)
solve("input/24.input",      assertPart1=386, assertPart2=4214)
