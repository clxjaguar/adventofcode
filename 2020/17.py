# cLx 2020 day 17

import copy
import itertools
import operator

class Cell():
	def __init__(self, coords):
		self.coords = coords

	def __repr__(self):
		return str(self.coords)

	def neighboursCoords(self):
		coordsList = []
		dimensions = len(self.coords)
		offsetList = itertools.product((-1, 0, +1), repeat=dimensions)
		for offsetPosition in offsetList:
			if offsetPosition == tuple([0]*dimensions): continue
			coordsList.append(tuple(map(operator.add, self.coords, offsetPosition)))
		return coordsList

class Universe():
	def __init__(self, dimensions=3):
		self.cells = {}
		self.age = 0
		self.dimensions=dimensions

	def initialyzeItPlanarFromFile(self, filename):
		lines = open(filename, 'r').read().split()
		for y in range(len(lines)):
			line = lines[y]
			for x in range(len(line)):
				if line[x] == '#':
					coords = (x, y)+tuple([0]*(self.dimensions-2))
					self.appendCell(coords)
		return self

	def appendCell(self, coords):
		self.cells[coords] = Cell(coords)

	def destroyCell(self, coords):
		del self.cells[coords]

	def iterate(self):
		# iterate the universe!
		nextUniverse = copy.deepcopy(self)
		nextUniverse.age+=1

		# make the list of the cells neighbourhood
		coordsNeighbours = {}
		for index in self.cells:
			cell = self.cells[index]
			if cell.coords not in coordsNeighbours:
				coordsNeighbours[cell.coords] = 0

			for c in cell.neighboursCoords():
				if c not in coordsNeighbours:
					coordsNeighbours[c] = 1
				else:
					coordsNeighbours[c]+= 1

		# apply evolution rules, as cruel as they are...
		for coords in coordsNeighbours:
			neighboursNbr = coordsNeighbours[coords]
			if coords in self.cells:
				if neighboursNbr < 2 or neighboursNbr > 3:
					del nextUniverse.cells[coords]
			else:
				# but sometimes magic happens!
				if neighboursNbr == 3:
					nextUniverse.cells[coords] = Cell(coords)

		return nextUniverse

	def __repr__(self):
		coords = set()
		mini = []; maxi = []
		for index in self.cells:
			cell = self.cells[index]
			for i in range(len(cell.coords)):
				if i >= len(maxi):
					maxi.append(cell.coords[i])
				else:
					maxi[i] = max(maxi[i], cell.coords[i])

				if i >= len(mini):
					mini.append(cell.coords[i])
				else:
					mini[i] = min(mini[i], cell.coords[i])

			coords.add(cell.coords)

		returnString = "Universe age: %d" % self.age

		if self.dimensions == 3:
			notPlanarDimensions = itertools.product(range(mini[2], maxi[2]+1))
		elif self.dimensions == 4:
			notPlanarDimensions = itertools.product(range(mini[2], maxi[2]+1), range(mini[3], maxi[3]+1))
		else:
			return "[learn how to code this plz]"

		for notPlanarCoordinates in notPlanarDimensions:
			returnString+="\nz=%d" % notPlanarCoordinates[0]
			if self.dimensions>3:
				returnString+=", w=%d" % notPlanarCoordinates[1]

			for y in range(mini[1], maxi[1]+1):
				returnString+="\n"
				for x in range(mini[0], maxi[0]+1):
					if (x, y)+notPlanarCoordinates in coords:
						returnString+="#"
					else:
						returnString+="."
			returnString+="\n"

		return returnString

def solve(filename, dimensions=3, verbose=False):
	print("\n*** %s ***" % filename)
	pocketDimension = Universe(dimensions).initialyzeItPlanarFromFile(filename)
	print("Dimensions:", pocketDimension.dimensions)

	while True:
		if verbose:
			print(pocketDimension)
		if pocketDimension.age == 6: break
		pocketDimension = pocketDimension.iterate()
	cellsNbr = len(pocketDimension.cells)
	print("%d cells at age %d" % (cellsNbr, pocketDimension.age))
	return cellsNbr

# part 1
assert solve("input/17.input.test", verbose=True) == 112
assert solve("input/17.input") == 247

# part 2
assert solve("input/17.input.test", dimensions=4, verbose=True) == 848
assert solve("input/17.input", dimensions=4) == 1392
