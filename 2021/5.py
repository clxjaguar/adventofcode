# cLx 2021 day 5

import sys
from collections import defaultdict

class VentsLine():
	def __init__(self, s):
		xy1, xy2 = s.strip().split(" -> ")
		self.x1, self.y1 = map(int, xy1.split(","))
		self.x2, self.y2 = map(int, xy2.split(","))

	def __repr__(self):
		return "%g,%g -> %g,%g" % (self.x1, self.y1, self.x2, self.y2)

	# Part 1
	def pointsListHV(self):
		if self.x1 == self.x2:
			return [(self.x1, y) for y in range(min(self.y1, self.y2), max(self.y1, self.y2)+1)]
		if self.y1 == self.y2:
			return [(x, self.y1) for x in range(min(self.x1, self.x2), max(self.x1, self.x2)+1)]
		return []

	# Part 2
	def pointsList(self):
		coords = self.pointsListHV()
		if len(coords) != 0:
			return coords

		dx = self.x2 - self.x1
		dy = self.y2 - self.y1

		if dx != dy and dx != -dy:
			raise ValueError("Not a 45° diagonal! %s" % self)

		def sign(i):
			if i < 0: return -1
			return 1

		for i in range(dx*sign(dx)+1):
			x = self.x1+i*sign(dx)
			y = self.y1+i*sign(dy)
			coords.append((x, y))

		return coords

def solve(filename, withDiagonals=False):
	fd = open(filename, 'r')

	lines = []
	for line in fd:
		lines.append(VentsLine(line))

	ventsMap = defaultdict(int)
	for line in lines:
		for x, y in line.pointsListHV() if not withDiagonals else line.pointsList():
			ventsMap[(x, y)]+= 1

	result = 0
	for xy in ventsMap:
		if ventsMap[xy] >= 2:
			result+=1

	print(result)
	return result

assert solve('input/5.input.test') == 5
assert solve('input/5.input') == 8111
assert solve('input/5.input.test', withDiagonals=True) == 12
assert solve('input/5.input',  withDiagonals=True) == 22088
