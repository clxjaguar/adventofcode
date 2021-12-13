# cLx 2021 day 13

import sys

def solve(filename):
	dots,folds = map(lambda l: l.strip().split("\n"), open(filename, 'r').read().split("\n\n"))
	dots = set(map(lambda c: tuple(map(int, c.split(","))), dots))
	folds = list(map(lambda f: f.replace("fold along ", "").split('='), folds))

	result1 = None
	for axis,axisPos in folds:
		axisPos = int(axisPos)
		newdots = set()
		for x, y in dots:
			if axis == 'x': # fold left vertical line
				if x > axisPos:
					x = 2*axisPos-x
			if axis == 'y': # fold up horizontal line
				if y > axisPos:
					y = 2*axisPos-y

			newdots.add((x, y))
		dots = newdots

		if result1 == None:
			result1 = len(dots)

	print(result1)

	for y in range(max([y for x, y in dots])+1):
		for x in range(max([x for x, y in dots])+1):
			sys.stdout.write("#" if (x, y) in dots else ' ')
		sys.stdout.write("\n")
	sys.stdout.write("\n")

	return result1

assert solve('input/13.input.test') == 17
assert solve('input/13.input') == 785
