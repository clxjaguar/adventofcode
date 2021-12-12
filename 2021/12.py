# cLx 2021 day 12

from collections import defaultdict

class Cave():
	def __init__(self, name):
		self.name = name
		self.links = {}
		self.small = 'a' <= name[0] <= 'z'
		
	def linkTo(self, name, destCave):
		self.links[name] = destCave

	def __repr__(self):
		return self.name

	def explore(self, exploredCaves=defaultdict(int), level=0, smallCaveTwiceFlag=True):
		exploredCaves[self]+=1
		# ~ print("  "*level + self.name, exploredCaves[self])
		
		if self.name == "end":
			return 1

		count = 0
		for caveName, cave in self.links.items():
			flag = smallCaveTwiceFlag
			if cave.small:
				if exploredCaves[cave] >= 2:
					continue
				if exploredCaves[cave] >= 1:
					if smallCaveTwiceFlag:
						continue
					flag = True
	
			count+=cave.explore(exploredCaves.copy(), level+1, flag)

		return count

def solve(filename, part2=False):
	caves = {}
	fd = open(filename, 'r')
	for line in fd:
		a, b = line.strip().split('-')
		
		for caveName in a, b:
			if caveName not in caves:
				caves[caveName] = Cave(caveName)
			
		for f, t in (a, b), (b, a):
			if f != "end" and t != "start":
				caves[f].linkTo(t, caves[t])

	result = caves['start'].explore(smallCaveTwiceFlag=not part2)
	print("%s: part%d=%d" % (filename, 2 if part2 else 1, result))
	return result

assert solve('input/12.input.test') == 10
assert solve('input/12.input')       == 4754
assert solve('input/12.input.test', part2=True) == 36
assert solve('input/12.input',       part2=True) == 143562
