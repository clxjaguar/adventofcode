# cLx 2022 day 12

import heapq
import sys
import time

VISUALIZATION = True

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


def solve(filename, refreshInterval=-1, assertPart1=None, assertPart2=None, doNotAcceptThesePart2=[]):
	fd = open(filename, 'r')

	field = {}
	for y, line in enumerate(fd):
		print(y, line.strip())
		for x, h in enumerate(line.strip()):
			if h == 'S':
				h = 'a'
				start = Node((x, y))
			elif h == 'E':
				h = 'z'
				target = Node((x, y))

			if 'a' <= h <= 'z':
				field[(x, y)] = int(ord(h) - ord('a'))
			else:
				raise Exception(h)

	width = max([x for x, y in field])+1
	height = max([y for x, y in field])+1

	print('\nstart:%s\ntarget:%s\n' % (start, target))
	time.sleep(1)

	def show(field, currentCoords=None, opened=set(), closed=set(), clearScreen=False):
		if not clearScreen:
			sys.stdout.write("\033[%dA" % (height+1))

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

				sys.stdout.write("%c" % (ord('a')+field[(x, y)]))

			sys.stdout.write("\x1B[0m\n")
		sys.stdout.write("\n")

	if VISUALIZATION:
		show(field, clearScreen=True)

	def pathFinder(field, target, start):
		part1 = None; part2 = None
		start, target = target, start

		lastTime = 0
		closedCoords = set()
		openedListCoords = set()
		openList = [start]
		heapq.heapify(openList)

		# A*
		while(len(openList)):
			u = heapq.heappop(openList)

			if VISUALIZATION:
				if time.time() > lastTime + refreshInterval:
					show(field, u.coords, openedListCoords, closedCoords)
					lastTime = time.time()
					time.sleep(0.1)

			if field[u.coords] == 0: # lowest level, for part 2
				if part2 == None or u.cost < part2:
					part2 = u.cost

			if u.coords == target.coords:
				if VISUALIZATION:
					show(field, u.coords, openedListCoords, closedCoords)
					# ~ print(u, target.coords)
				if part1 == None or u.cost < part1:
					part1 = u.cost
				if part2 not in doNotAcceptThesePart2:
					return part1, part2
			for coords in u.neighborsCoords():
				if not(0 <= coords[0] < width and 0 <= coords[1] < height) or coords in closedCoords: continue

				if field[coords] < field[u.coords] - 1: continue # too high to climb!
				v = Node(coords, cost=u.cost + 1)
				v.heuristics = v.cost + abs(v.coords[0] - target.coords[0]) + abs(v.coords[1] - target.coords[1])
				# ~ v.heuristics = v.cost + (field[u.coords] - field[v.coords])
				# ~ v.heuristics = v.cost + (field[u.coords] - field[v.coords]) + abs(v.coords[0] - target.coords[0]) + abs(v.coords[1] - target.coords[1])
				heapq.heappush(openList, v)
				if VISUALIZATION:
					openedListCoords.add(v.coords)

			closedCoords.add(u.coords)
		return part1, part2

	part1, part2 = pathFinder(field, target, start)

	print("Result of %s (part 1): %d" % (filename, part1))
	print("Result of %s (part 2): %d" % (filename, part2))

	if assertPart1:
		assert part1 == assertPart1
	if assertPart2:
		assert part2 == assertPart2
	time.sleep(2)


solve('input/12.input.test', assertPart1=31, assertPart2=29, doNotAcceptThesePart2=[30])
solve('input/12.input', assertPart1=339, assertPart2=332, refreshInterval=0.25)
solve('input/12.input2', assertPart1=468, assertPart2=459, refreshInterval=0.25, doNotAcceptThesePart2=[461])
