# cLx 2021 day 14

from collections import defaultdict

def solve(filename):
	fd = open(filename)
	template = fd.readline().strip()

	chainContents = defaultdict(int)
	for i in range(len(template)-1):
		pair = template[i:i+2]
		chainContents[pair]+=1

	pairInsertionRules = {}
	for line in fd:
		line = line.strip()
		if len(line):
			pair, insert = line.split(' -> ')
			pairInsertionRules[pair] = insert

	for i in range(1, 40+1):
		for pair, amount in chainContents.copy().items():
			if amount < 1:
				continue
			insert = pairInsertionRules[pair]
			chainContents[pair]-=amount

			chainContents[pair[0]+insert]+=amount
			chainContents[insert+pair[1]]+=amount

		def countMaxMinusMin():
			elements = defaultdict(int)
			for pair, amount in chainContents.items():
				elements[pair[1]]+=amount
			elements[template[0]]+=1
			return max(elements.values())-min(elements.values())

		if i == 10: result1 = countMaxMinusMin()
		if i == 40: result2 = countMaxMinusMin()

	print("%s: Part 1: %d" % (filename, result1))
	print("%s: Part 2: %d" % (filename, result2))
	return result1, result2

assert solve('input/14.input.test') == (1588, 2188189693529)
assert solve('input/14.input')      == (2408, 2651311098752)
