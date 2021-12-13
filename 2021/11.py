# cLx 2021 day 11

import sys

def solve(filename):
	fd = open(filename, 'r')

	octopuses = {(x, y):int(v) for y,line in enumerate(fd) for x, v in enumerate(line.strip())}

	def show(octopuses, flashed=set()):
		for y in range(max([y for x, y in octopuses])+1):
			for x in range(max([x for x, y in octopuses])+1):
				if (x, y) in flashed:
					sys.stdout.write("\x1B[7m")
				sys.stdout.write("%X" % octopuses[(x, y)])
				sys.stdout.write("\x1B[0m")
			sys.stdout.write("\n")
		sys.stdout.write("\n")
	show(octopuses)

	totalFlashes = 0
	for i in range(1, 1000):
		# first, the energy level of each octopus increases by 1.
		for coords in octopuses:
			octopuses[coords]+=1

		# then, any octopus with an energy level greater than 9 flashes
		flashed = set()
		cont=True
		while cont:
			cont=False
			for x, y in octopuses:
				if octopuses[(x, y)] > 9 and (x, y) not in flashed:
					flashed.add((x, y))
					cont=True

					for dx, dy in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
						if (x+dx, y+dy) not in octopuses:
							continue
						octopuses[(x+dx, y+dy)]+=1

		# any octopus that flashed during this step has its energy level set to 0
		for coords in flashed:
			octopuses[coords] = 0

		totalFlashes+=len(flashed)
		print("After step %d: %d flashed, %d total flashes" % (i, len(flashed), totalFlashes))
		if i == 100:
			result1 = totalFlashes
		show(octopuses, flashed)

		if len(flashed) == len(octopuses):
			result2 = i
			break

	print("%s: Part 1: %d\tPart 2: %d" % (filename, result1, result2))
	return result1, result2

assert solve('input/11.input.test') == (1656, 195)
assert solve('input/11.input')      == (1659, 227)
