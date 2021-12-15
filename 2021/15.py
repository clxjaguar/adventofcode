# cLx 2021 day 15

import heapq
import sys
import time

VISUALIZATION = False

class Node():
	def __init__(self, coords, cost=0):
		self.coords = coords
		self.cost = cost
		self.heuristics = 0

	def neighborsCoords(self):
		x, y = self.coords
		return ((x+1, y), (x, y+1), (x, y-1), (x-1, y))

	def __lt__(self, otherNode):
		return self.heuristics < otherNode.heuristics

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

	startTime = time.time()

	def show(field, currentCoords=None, opened=set(), closed=set(), clearScreen=False):
		if clearScreen:
			sys.stdout.write("\x1B[2J") # clear screen
		sys.stdout.write("\x1B[H") # move cursor
		for y in range(height):
			for x in range(width):
				if (x, y) == currentCoords:
					sys.stdout.write("\x1B[97m\x1B[42m")
				elif (x, y) in closed:
					sys.stdout.write("\x1B[97m\x1B[100m")

				elif (x, y) in opened:
					sys.stdout.write("\x1B[91m\x1B[46m")
				else:
					sys.stdout.write("\x1B[97m\x1B[44m")

				sys.stdout.write("%X" % field[(x, y)])

			sys.stdout.write("\x1B[0m\n")
		sys.stdout.write("\n")

	start = Node((0, 0))
	target = Node((width-1, height-1))

	if VISUALIZATION:
		show(field, clearScreen=True)

	def pathFinder(field, target, start):
		lastTime = 0
		closedCoords = set()
		openedListCoords = set()
		openList = [start]
		heapq.heapify(openList)

		while(len(openList)):
			u = heapq.heappop(openList)

			if VISUALIZATION:
				if time.time() > lastTime + refreshInterval:
					show(field, u.coords, openedListCoords, closedCoords)
					lastTime = time.time()
					time.sleep(0.01)

			if u.coords == target.coords:
				if VISUALIZATION:
					show(field, u.coords, openedListCoords, closedCoords)
				return u.cost
			for coords in u.neighborsCoords():
				if not(0 <= coords[0] < width and 0 <= coords[1] < height) or coords in closedCoords: continue
				v = Node(coords, cost=u.cost + field[coords])
				v.heuristics = v.cost + abs(v.coords[0] - target.coords[0]) + abs(v.coords[1] - target.coords[1])
				heapq.heappush(openList, v)
				if VISUALIZATION:
					openedListCoords.add(v.coords)

			closedCoords.add(u.coords)

	result = pathFinder(field, target, start)
	print("%s (part %d): %d (%.4fs)" % (filename, 2 if part2 else 1, result, time.time() - startTime))
	time.sleep(1)
	return result


assert solve('input/15.input.test')                                  ==   40
assert solve('input/15.input'     , refreshInterval=.03)             ==  410
assert solve('input/15.input.test', refreshInterval=.02, part2=True) ==  315
assert solve('input/15.input',      refreshInterval=2,   part2=True) == 2809
