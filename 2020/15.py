# cLx 2020 day 15

import utils

def solve(startingNumbers, nth=2020):
	utils.start()
	i = 0
	spokenNumbers = {}
	spokenNumbersBefore = {}

	while i < len(startingNumbers):
		number = startingNumbers[i]; i+=1
		if number in spokenNumbers:
			spokenNumbersBefore[number] = spokenNumbers[number]
		spokenNumbers[number] = i

	while i != nth:
		i+=1

		if number in spokenNumbersBefore:
			number = spokenNumbers[number] - spokenNumbersBefore[number]
		else:
			number = 0

		try: spokenNumbersBefore[number] = spokenNumbers[number]
		except: pass

		spokenNumbers[number] = i

	print("%d (%.2fms)" % (number, utils.stop()))
	return number

# part 1
assert solve([0, 3, 6]) == 436
assert solve([1, 3, 2]) == 1
assert solve([1, 2, 3]) == 27
assert solve([2, 3, 1]) == 78
print("\nPart 1 answer:")
assert solve([0,13,1,8,6,15]) == 1618

# part 2
print("\nPart 2 answer:")
assert solve([0,13,1,8,6,15], 30000000) == 548531
