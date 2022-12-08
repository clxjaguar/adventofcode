# cLx 2022 day 8

class Tree():
	def __init__(self, height):
		self.height = int(height)
		self.visible = False


class TreeMap():
	def __init__(self):
		self.width = 0
		self.length = 0
		self.trees = {}

	def addLineOfTrees(self, line):
		if len(line) > self.width: self.width = len(line)
		for n, c in enumerate(line):
			self.trees[(n, self.length)] = Tree(height=c)
		self.length+=1

	def calculateVisibility(self):
		for y in range(self.length):
			# view from the west
			lastHeight = -1
			for x in range(self.width):
				t = self.trees[(x, y)]
				if t.height > lastHeight:
					t.visible = True
					lastHeight = t.height

			# view from the east
			lastHeight = -1
			for x in range(self.width-1, -1, -1):
				t = self.trees[(x, y)]
				if t.height > lastHeight:
					t.visible = True
					lastHeight = t.height

		for x in range(self.width):
			# view from the north
			lastHeight = -1
			for y in range(self.length):
				t = self.trees[(x, y)]
				if t.height > lastHeight:
					t.visible = True
					lastHeight = t.height

			# view from the south
			lastHeight = -1
			for y in range(self.length-1, -1, -1):
				t = self.trees[(x, y)]
				if t.height > lastHeight:
					t.visible = True
					lastHeight = t.height

	def countVisiblesTrees(self):
		count = 0
		for y in range(self.length):
			for x in range(self.width):
				if self.trees[(x, y)].visible:
					count+=1
		return count

	def calculateScenicScoreOfTree(self, tree_x, tree_y):
		# looking north
		viewRangeNorth = 0; x = tree_x
		for y in range(tree_y-1, -1, -1):
			viewRangeNorth+=1
			if self.trees[(x, y)].height >= self.trees[(tree_x, tree_y)].height:
				break

		# looking west
		viewRangeWest = 0; y = tree_y
		for x in range(tree_x-1, -1, -1):
			viewRangeWest+=1
			if self.trees[(x, y)].height >= self.trees[(tree_x, tree_y)].height:
				break

		# looking east
		viewRangeEast = 0; y = tree_y
		for x in range(tree_x+1, self.width):
			viewRangeEast+=1
			if self.trees[(x, y)].height >= self.trees[(tree_x, tree_y)].height:
				break

		# looking south
		viewRangeSouth = 0; x = tree_x
		for y in range(tree_y+1, self.length):
			viewRangeSouth+=1
			if self.trees[(x, y)].height >= self.trees[(tree_x, tree_y)].height:
				break

		scenicScore = viewRangeNorth * viewRangeWest * viewRangeEast * viewRangeSouth
		return scenicScore

	def findBestScenicScore(self):
		bestScore = 0
		for y in range(self.length):
			for x in range(self.width):
				score = self.calculateScenicScoreOfTree(x, y)
				if score > bestScore:
					bestScore = score
		return bestScore

	def __str__(self):
		def hightlight(inpt, cond, before, after):
			if cond: return before+str(inpt)+after
			return str(inpt)

		returnString = "\n"
		for y in range(self.length):
			returnString+= "  "
			for x in range(self.width):
				t = self.trees[(x, y)]
				returnString+=hightlight(t.height, t.visible, '\033[31m', '\033[39m')
			returnString+="\n"
		return returnString


def solve(filename, assertPart1=None, assertPart2=None):
	fd = open(filename, 'r')

	treeMap = TreeMap()
	for line in fd:
		treeMap.addLineOfTrees(line.strip())

	treeMap.calculateVisibility()
	print(treeMap)

	# Part 1
	part1 = treeMap.countVisiblesTrees()
	print("Part 1 of %s:" % filename, part1)
	if assertPart1 != None:
		assert part1 == assertPart1

	# Part 2
	part2 = treeMap.findBestScenicScore()
	print("Part 2 of %s:" % filename, part2)
	if assertPart2 != None:
		assert part2 == assertPart2


solve('input/8.input.test', assertPart1=21, assertPart2=8)
solve('input/8.input',      assertPart1=1705, assertPart2=371200)
