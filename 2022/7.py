# cLx 2022 day 7

class Directory():
	def __init__(self, parent, name):
		self.name = name
		if parent == None:
			self.path = '/'
		elif parent.parent == None:
			self.path = '/' + name
		else:
			self.path = parent.path + '/' + name

		self.parent = parent
		self.files = {}
		self.subDirectories = {}
		self.listed = False

	def newFile(self, name, size):
		self.files[name] = size

	def newDir(self, name):
		self.subDirectories[name] = Directory(self, name)

	def getSize(self):
		global sizeCount
		size = 0
		for name in self.files:
			size+=self.files[name]
		for name in self.subDirectories:
			dirSize = self.subDirectories[name].getSize()
			size+=dirSize
			if dirSize <= 100000:
				sizeCount+=dirSize
		dirListDict[self.path] = size
		return size

def solve(filename, assertPart1=None, assertPart2=None):
	global sizeCount, dirListDict
	dirListDict = {}
	sizeCount = 0

	fd = open(filename, 'r')

	for line in fd:
		if line[0] == '$':
			command = line[1:].strip().split()
			if command[0] == 'cd':
				if command[1] == '/':
					rootDir = Directory(None, '/')
					currentDir = rootDir

				elif command[1] == '..':
					currentDir = currentDir.parent

				else:
					currentDir = currentDir.subDirectories[command[1]]

				# ~ print("Current directory is %s" % currentDir.path)
			if command == 'ls':
				currentDir.listed = True

		else:
			assert command == ['ls']
			size, name = line.strip().split()
			if size == 'dir':
				currentDir.newDir(name)
			else:
				currentDir.newFile(name, int(size))

	# Part 1
	usedSize = rootDir.getSize()
	print("part 1 of", filename, sizeCount)
	if assertPart1 != None:
		assert sizeCount == assertPart1

	# Part 2
	totalDiskSize = 70000000; neededFreeSize = 30000000
	delectionSizeNeeded = usedSize - (totalDiskSize - neededFreeSize)

	for size in sorted(dirListDict.values()):
		if size >= delectionSizeNeeded:
			break
	else:
		raise Exception()

	print("part 2 of", filename, size)
	if assertPart2 != None:
		assert size == assertPart2


solve('input/7.input.test', assertPart1=95437,   assertPart2=24933642)
solve('input/7.input',      assertPart1=1783610, assertPart2=4370655)
