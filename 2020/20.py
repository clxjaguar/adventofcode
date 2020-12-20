import numpy
import copy

def binaryMirror(val, len=10):
	s = ""
	for i in range(len):
		s+= ("1" if (val & (2**i)) else "0")
	return int(s, 2)

N=0; E=1; S=2; W=3
class Tile():
	def __init__(self, tId, lines):
		self.id = tId
		self.borders = []
		self.borders.append([])
		self.bordersMatches = [set(),set(),set(),set()]
		self.coords = {}
		content = []
		numContent = []
		l = ""; r = ""
		for line in lines:
			line = line.replace(".", "0").replace("#", "1")
			contentTmp = tuple()
			for c in line:
				contentTmp = contentTmp+(c,)
			content.append(contentTmp[1:-1])
			l+=line[0]; r+=line[-1]
			numContent.append(int(line, 2))

		self.content = numpy.array(content[1:-1])

		self.borders[0].append(numContent[0])  # N
		self.borders[0].append(int(r, 2))      # E
		self.borders[0].append(numContent[-1]) # S
		self.borders[0].append(int(l, 2))      # W

		for i in range(3):
			bords = []
			bords.append(binaryMirror(self.borders[i][W]))
			bords.append(self.borders[i][N])
			bords.append(binaryMirror(self.borders[i][E]))
			bords.append(self.borders[i][S])
			self.borders.append(bords)

		for i in range(4):
			bords = []
			bords.append(self.borders[i][S])
			bords.append(binaryMirror(self.borders[i][E]))
			bords.append(self.borders[i][N])
			bords.append(binaryMirror(self.borders[i][W]))
			self.borders.append(bords)

	def getBorder(self, bord, pos):
		return self.borders[pos][bord]

	def __repr__(self):
		retStr = ""
		for pos in self.coords:
			retStr+="coords=%s (pos %d) " % (str(self.coords[pos]), pos)
		return retStr

def loadTiles(filename):
	tiles = {}
	tilesStr = open(filename).read().split("\n\n")

	for tileStr in tilesStr:
		lines = tileStr.strip().split("\n")
		tId = int(lines[0].split()[1].replace(":", ""))
		tiles[tId] = Tile(tId, lines[1:])
	return tiles

def solve(filename, assertPart1=None, assertPart2=None):
	tiles = loadTiles(filename)
	for idx in tiles:
		tile = tiles[idx]
		for idx2 in tiles:
			if idx2 == idx:
				continue
			tile2 = tiles[idx2]
			for pos in range(8):
				if tile.getBorder(bord=N, pos=0) == tile2.getBorder(bord=S, pos=pos):
					tile.bordersMatches[N].add((pos, idx2))
				if tile.getBorder(bord=E, pos=0) == tile2.getBorder(bord=W, pos=pos):
					tile.bordersMatches[E].add((pos, idx2))
				if tile.getBorder(bord=S, pos=0) == tile2.getBorder(bord=N, pos=pos):
					tile.bordersMatches[S].add((pos, idx2))
				if tile.getBorder(bord=W, pos=0) == tile2.getBorder(bord=E, pos=pos):
					tile.bordersMatches[W].add((pos, idx2))

	p = 1
	cornerTiles = []
	for idx in tiles:
		tile = tiles[idx]
		notMatchingBordersNbr = 0
		for bord in tile.bordersMatches:
			matches = len(bord)
			assert matches <= 1
			if matches == 0:
				notMatchingBordersNbr+=1

		if notMatchingBordersNbr == 2:
			cornerTiles.append(idx)
			p*=idx

	print("Product of corners tiles ids:", p)
	if assertPart1 != None:
		assert p == assertPart1

	# part 2
	tilesCoords = {}
	for idx in cornerTiles:
		if len(tiles[idx].bordersMatches[N]) == 0 and len(tiles[idx].bordersMatches[W]) == 0:
			tiles[idx].coords[0] = (0, 0); tilesCoords[(0, 0)] = (idx, 0)
			break

	size=int(len(tiles)**.5)

	pos = tilesCoords[(0, 0)][1]
	x = 1; y = 0;
	while(x < size):
		tile = tiles[idx]
		# ~ print("*** tile:", tile.id)

		ok = False

		for idx2 in tiles:
			if idx2 == idx:
				continue
			tile2 = tiles[idx2]
			for pos2 in range(8):
				if tile.getBorder(bord=E, pos=pos) == tile2.getBorder(bord=W, pos=pos2):
					# ~ print("* pos2=", idx2)
					ok = True
					tiles[idx2].coords[pos2] = (x, y)
					tilesCoords[(x, y)] = (idx2, pos2)
					pos = pos2
					idx = idx2
					break
			if ok: break
		if not ok:
			print("Error: border not found")
			exit(-1)
		x+=1

	for x in range(size):
		idx, pos = tilesCoords[(x, 0)]

		y = 1;
		while(y < size):
			tile = tiles[idx]
			ok = 0
			for idx2 in tiles:
				if idx2 == idx:
					continue
				tile2 = tiles[idx2]
				for pos2 in range(8):
					if tile.getBorder(bord=S, pos=pos) == tile2.getBorder(bord=N, pos=pos2):
						ok+=1
						tiles[idx2].coords[pos2] = (x, y)
						tilesCoords[(x, y)] = (idx2, pos2)
						pos = pos2
						idx = idx2
						break;
				if ok: break
			if ok > 1:
				print("Error: not single solution found:", x, y)
				exit(-1)
			if ok == 0:
				print("Error: border not found")
				exit(-1)
			y+=1

	# ~ print(tiles[2729].content); exit(1)

	usedId = set()
	for y in range(size):
		print("-"+"------------"*size)
		print("|"+"           |"*size)
		line1 = "|"
		line2 = "|"
		for x in range(size):
			line1+= " x=%2d y=%2d |" % (x, y)
			line2+= " %5d (%d) |" % (tilesCoords[(x, y)])
			if tilesCoords[(x, y)] not in usedId:
				usedId.add(tilesCoords[(x, y)])
			else:
				print("ERROR:", tilesCoords[(x, y)])
				exit(2)
		print(line1)
		print(line2)
		print("|"+"           |"*size)
	print("-"+"------------"*size)


	vstack = None
	for y in range(size):
		hstack = None
		for x in range(size):
			# ~ print(x, y)
			idx, pos = tilesCoords[(x,y)]
			# ~ print("%d: %s" % (idx, tiles[idx]))
			content = tiles[idx].content
			if pos%4 > 0:
				content = numpy.rot90(tiles[idx].content, k=-(pos%4))
				# ~ print("rotate", x, y, "(pos=%d)"%(pos%4))
			if pos>=4:
				content = numpy.flip(content, axis=0)
				# ~ print("flip", x, y)
			# ~ print(content)
			if x == 0:
				hstack = content
			else:
				hstack = numpy.hstack((hstack, content))
		if y == 0:
			vstack = hstack
		else:
			vstack = numpy.vstack((vstack, hstack))
	bigArray = vstack

	sm = (("                  # "),
          ("#    ##    ##    ###"),
          (" #  #  #  #  #  #   "))

	smCoords = set()
	for y, line in enumerate(sm):
		for x, c in enumerate(line):
			if c == '#':
				smCoords.add((x, y))

	for gpos in range(8):
		bigArray2 = copy.deepcopy(bigArray)
		bigArray2 = numpy.rot90(bigArray2, k=-(gpos%4))
		if gpos >= 4:
			bigArray2 = numpy.flip(bigArray2, axis=0)

		# ~ for i in range(size*8):
			# ~ print("%3d"%i, "".join(bigArray[i]).replace("0", ".").replace("1", "#"))

		print("Global reposition:", gpos)
		smFounds = 0

		for y in range(size*8-2):
			for x in range(size*8-19):
				ok = True
				for xx, yy in smCoords:
					smPresent = bigArray2[y+yy][x+xx]
					if int(smPresent) != 1:
						ok = False
						break
				if ok:
					smFounds+=1
					for xx, yy in smCoords:
						bigArray2[y+yy][x+xx] = 2

					cnt = 0
					for yyy in range(size*8):
						for xxx in range(size*8):
							c = int(bigArray2[yyy][xxx])
							if c==1:
								cnt+=1
					print("SeeMonster %d found at (%d, %d): water roughness remaining %d" % (smFounds, x, y, cnt))
		if smFounds > 0:
			print(smCoords)
			for i in range(size*8):
				print("%3d"%i, "".join(bigArray2[i]).replace("0", ".").replace("1", "#").replace("2", "O"))
			print()
			for y, line in enumerate(sm):
				print("    ", line)
			print()
			print(cnt)
			if assertPart2:
				assert cnt == assertPart2
			# ~ exit()

solve("input/20.input.test", assertPart1=20899048083289, assertPart2=273)
solve("input/20.input",      assertPart1=4006801655873,  assertPart2=1838)
# < 2138
# < 1913
