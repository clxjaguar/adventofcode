# cLx 2021 day 15

import sys
import time

class Node():
	def __init__(self, coords, cost=0):
		self.coords = coords
		self.cost = cost
		self.heuristics = 0

	def neighborsCoords(self):
		x, y = self.coords
		return ((x+1, y), (x, y+1), (x, y-1), (x-1, y))

	def __lt__(self, otherNode):
		return self.heuristics > otherNode.heuristics

	def __repr__(self):
		return "(%g, %g): C=%g H=%g" % (self.coords[0], self.coords[1], self.cost, self.heuristics)


def solve(filename, part2=False, refreshInterval=-1):
	fd = open(filename, 'r')
	field = {(x, y):int(v) for y,line in enumerate(fd) for x, v in enumerate(line.strip())}
	width = max([x for x, y in field])+1
	height = max([y for x, y in field])+1

	if part2:
		for i in range(5):
			for j in range(5):
				if i == 0 and j == 0:
					continue
				for x in range(width):
					for y in range(height):
						val = field[(x, y)] + i + j
						while val > 9:
							val-=9
						field[(i*width+x, j*height+y)] = val
		width*=5; height*=5

	def show(field, currentCoords=None, highlight=set(), visited=set(), clearScreen=False):
		if clearScreen:
			sys.stdout.write("\x1B[2J") # clear screen
		sys.stdout.write("\x1B[H") # move cursor
		for y in range(height):
			for x in range(width):
				if (x, y) == currentCoords:
					sys.stdout.write("\x1B[97m\x1B[42m")
				else:
					if (x, y) in highlight: sys.stdout.write("\x1B[91m")
					else:                   sys.stdout.write("\x1B[97m")
					if (x, y) in visited:   sys.stdout.write("\x1B[100m")
					else:                   sys.stdout.write("\x1B[44m")
				try:
					sys.stdout.write("%X" % field[(x, y)])
				except:
					sys.stdout.write(".")

			sys.stdout.write("\x1B[0m\n")
		sys.stdout.write("\n")

	start = Node((0, 0))
	target = Node((width-1, height-1))

	show(field, clearScreen=True)

	def pathFinder(field, target, start):
		lastTime = time.time()
		closedCoords = set()
		openList = []
		openList.append(start)

		while(len(openList)):
			openList.sort()
			u = openList.pop()

			if time.time() > lastTime + refreshInterval:
				lastTime = time.time()
				show(field, u.coords, [n.coords for n in openList], closedCoords)
				time.sleep(0.02)

			if u.coords == target.coords:
				print(u.cost)
				return u.cost
			for coords in u.neighborsCoords():
				if coords not in field: continue
				if coords in closedCoords: continue
				for node in openList:
					if node.coords == coords:
						if node.cost < u.cost: continue
				v = Node(coords, cost=u.cost + field[coords])
				v.heuristics = v.cost + abs(v.coords[0] - target.coords[0]) + abs(v.coords[1] - target.coords[1])
				openList.append(v)

			closedCoords.add(u.coords)

	result = pathFinder(field, target, start)
	return result


assert solve('input/15.input.test')                                  ==   40
assert solve('input/15.input'     , refreshInterval=.50)             ==  410
assert solve('input/15.input.test', refreshInterval=.07, part2=True) ==  315
assert solve('input/15.input',      refreshInterval=600, part2=True) == 2809
