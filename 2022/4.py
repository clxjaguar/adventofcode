# cLx 2022 day 4

def solve1(filename):
	fd = open(filename, 'r')
	count = 0
	for line in fd:
		first, second = line.strip().split(',')
		firstMin, firstMax = map(int, first.split('-'))
		secondMin, secondMax = map(int, second.split('-'))

		if (firstMin >= secondMin and firstMax <= secondMax) or (secondMin >= firstMin and secondMax <= firstMax):
			count+=1

	print(count)
	return count

def solve2(filename):
	fd = open(filename, 'r')
	count = 0
	for line in fd:
		first, second = line.strip().split(',')
		firstMin, firstMax = map(int, first.split('-'))
		secondMin, secondMax = map(int, second.split('-'))

		if (firstMin >= secondMin and firstMax <= secondMax) or (secondMin >= firstMin and secondMax <= firstMax):
			count+=1
		elif (secondMin <= firstMin <= secondMax) or (secondMin <= firstMax <= secondMax):
			count+=1

	print(count)
	return count

assert solve1('input/4.input.test') == 2
assert solve1('input/4.input') == 490
assert solve2('input/4.input.test') == 4
assert solve2('input/4.input') == 921
