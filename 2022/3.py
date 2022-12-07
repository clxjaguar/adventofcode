# cLx 2022 day 3

def solve1(filename):
	fd = open(filename, 'r')
	prioritySum = 0

	for line in fd:
		line = line.strip()
		h = len(line) // 2
		a = line[0:h]
		b = line[h:]
		assert len(a) == len(b)

		a, b = set(a), set(b)
		c = a.intersection(b)
		assert len(c) == 1
		c = c.pop()

		if ord('a') <= ord(c) <= ord('z'):
			priority = ord(c) - ord('a') + 1
		elif ord('A') <= ord(c) <= ord('Z'):
			priority = ord(c) - ord('A') + 27
		else:
			raise Exception()

		prioritySum+=priority

	print(prioritySum)
	return prioritySum


def solve2(filename):
	fd = open(filename, 'r')
	prioritySum = 0

	while True:
		a = set(fd.readline().strip())
		b = set(fd.readline().strip())
		c = set(fd.readline().strip())
		if not c:
			break

		c = a.intersection(b).intersection(c)
		assert len(c) == 1
		c = c.pop()

		if ord('a') <= ord(c) <= ord('z'):
			priority = ord(c) - ord('a') + 1
		elif ord('A') <= ord(c) <= ord('Z'):
			priority = ord(c) - ord('A') + 27
		else:
			raise Exception()

		prioritySum+=priority

	print(prioritySum)
	return prioritySum

assert solve1('input/3.input.test') == 157
assert solve1('input/3.input') == 7917
assert solve2('input/3.input.test') == 70
assert solve2('input/3.input') == 2585
