# cLx 2020 day 15

import utils

def solve(startingNumbers, nth=2020):
	utils.start()
	i = 0
	spokenNumbers = {}
	try:
		while True:
			i+=1
			if startingNumbers:
				number = startingNumbers.pop(0)
			else:
				if number not in spokenNumbers:
					number = 0
				elif len(spokenNumbers[number]) < 2:
					number = 0
				else:
					number = spokenNumbers[number][-1] - spokenNumbers[number][-2]

			if number not in spokenNumbers:
				spokenNumbers[number] = []
			spokenNumbers[number].append(i)

			if i == nth:
				print("%d (%.2fms)" % (number, utils.stop()))
				return number
	except KeyboardInterrupt:
		print("Killed at", i)

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
