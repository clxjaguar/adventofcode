import copy

class PuzzleMap():
	def __init__(self, filename):
		fd = open(filename, 'r')
		self.xSize = 0
		self.ySize = 0
		self.generation = 0

		self.M = []
		for line in fd:
			line = line.strip()
			if line:
				L = []
				for c in line:
					L.append(c)
				self.M.append(L)
				if len(line) > self.xSize:
					self.xSize = len(line)
				self.ySize+=1
		fd.close()

	def __str__(self):
		r = ""
		for L in self.M:
			r+="\n"+("".join(L))
		return(r)

	def checkPos(self, x, y, default=None):
		if x<0 or y<0:
			if default == None:
				raise IndexError
			return default
		try:
			return self.M[y][x]
		except:
			return default

	def setPos(self, x, y, c):
		if x<0 or y<0 or x>self.xSize or y>self.ySize:
			raise IndexError("MAIS NE DESSINE PAS SUR LA TABLE VOYONS!")
		self.M[y][x] = c

	def copy(self):
		copiedMap = copy.deepcopy(self)
		copiedMap.generation+=1
		return copiedMap
