# cLx 2020 day 11

import utils

aroundIndexes = ((-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0))

def countPeopleInSight(M, x, y):
	peopleInSight = 0
	for adj in aroundIndexes:
		i = 1; c = '.'
		while c == '.':
			c = M.checkPos(x+adj[0]*i,y+adj[1]*i, "$")
			if c == '#': peopleInSight+=1
			i+=1
	return peopleInSight

def countPeopleAroundThisSeat(M, x, y):
	peopleAround = 0
	for adj in aroundIndexes:
		if M.checkPos(x+adj[0], y+adj[1], ".") == '#':
			peopleAround+=1
	return peopleAround

def solve(filename, peopleAroundCountingFunction, peopleAroundThreshold):
	M = utils.PuzzleMap(filename)

	mapChanged = True
	while mapChanged:
		print("Gen:", M.generation, M)
		N = M.copy()
		peopleInMap = 0
		mapChanged = False
		for x in range(M.xSize):
			for y in range(M.ySize):
				c = M.checkPos(x, y)
				if c == '#': peopleInMap+=1

				p = peopleAroundCountingFunction(M, x, y)
				if c == 'L' and p == 0:
					N.setPos(x, y, "#");
					mapChanged=True
				elif c == '#' and p >= peopleAroundThreshold:
					N.setPos(x, y, "L");
					mapChanged=True
		M = N
		print()
	print("Occupied seats:", peopleInMap)
	return peopleInMap

def main():
	# part 1
	assert solve("input/11.input.test", countPeopleAroundThisSeat, 4) == 37
	assert solve("input/11.input", countPeopleAroundThisSeat, 4) == 2296

	# part 2
	assert solve("input/11.input.test", countPeopleInSight, 5) == 26
	assert solve("input/11.input", countPeopleInSight, 5) == 2089

if __name__ == "__main__":
	main()
