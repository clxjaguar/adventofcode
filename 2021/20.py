# cLx 2021 day 20

import sys

def solve(filename):
	fd = open(filename)
	alg = fd.readline().strip()
	fd.readline()

	field = set()
	for y,line in enumerate(fd):
		for x, v in enumerate(line.strip()):
			if v == '#':
				field.add((x, y))

	min_x, max_x = 0, max([x for x, y in field])
	min_y, max_y = 0, max([y for x, y in field])

	def show(field):
		for y in range(min_y, max_y+1):
			for x in range(min_x, max_x+1):
				if (x, y) in field:
					sys.stdout.write("#")
				else:
					sys.stdout.write(".")

			sys.stdout.write("\n")
		sys.stdout.write("\n")

	def step():
		default = '0'
		if (min_x, min_y) in field:
			default = '1'
		def getVal(i, j):
			bits = ''
			for y in (j-1, j, j+1):
				for x in (i-1, i, i+1):
					# unknown universe!
					if x < min_x or x > max_x or y < min_y or y > max_y:
						bits+=default
					else:
						bits+= '1' if (x, y) in field else '0'
			return int(bits, 2)

		nextField = set()
		for y in range(min_y-1, max_y+2):
			for x in range(min_x-1, max_x+2):
				val = getVal(x, y)
				if alg[val] == '#':
					nextField.add((x, y))
		return nextField

	show(field)

	for i in range(1, 50+1):
		min_x, max_x = min_x-1, max_x+1
		min_y, max_y = min_y-1, max_y+1
		field = step()

		if i == 2:
			result1 = len(field)
			show(field)
		if i == 50:
			result2 = len(field)
			show(field)
		print("Iteration #%d, %d cells" % (i, len(field)))

	print("%s: Part 1 = %d\tPart 2 = %d" % (filename, result1, result2))
	return result1, result2

assert solve('input/20.input.test') == (35, 3351)
assert solve('input/20.input') == (5464, 19228)
