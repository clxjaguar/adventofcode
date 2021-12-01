# cLx 2021 day 1

def solve1(filename):
	inpt = tuple(map(int, open(filename, 'r').read().split()))
	depthIncreasedTimes = 0
	for i in range(1, len(inpt)):
		if inpt[i] > inpt[i-1]:
			depthIncreasedTimes+=1
	return depthIncreasedTimes

def solve2(filename):
	inpt = tuple(map(int, open(filename, 'r').read().split()))
	depthIncreasedTimes = 0
	lastDepth=float('nan')
	for i in range(0, len(inpt)-2):
		depth = sum(inpt[i:i+3])
		if depth > lastDepth:
			depthIncreasedTimes+=1
		lastDepth = depth
	return depthIncreasedTimes


assert solve1('input/1.input.test') == 7
assert solve1('input/1.input') == 1292
assert solve2('input/1.input.test') == 5
assert solve2('input/1.input') == 1262
