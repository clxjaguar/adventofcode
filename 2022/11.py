# cLx 2022 day 11

import re

class Monkey():
	def __init__(self, items, operation, testDivisor, ifDivisibleThrowTo, ifNotDivisibleThrowTo):
		self.items = items
		# ~ print(self.items)

		self.testDivisor = testDivisor
		self.ifDivisibleThrowTo = ifDivisibleThrowTo; self.ifNotDivisibleThrowTo = ifNotDivisibleThrowTo

		operator, value = re.search('new = old ([\*\+])\s+([0-9]+|old)', operation).groups()
		if operator == '*' and value == 'old':   self.operation = lambda x: x**2
		elif operator == '+' and value == 'old':   self.operation = lambda x: x+x
		elif operator == '*':                    self.operation = lambda x: x*int(value)
		elif operator == '+':                    self.operation = lambda x: x+int(value)
		else:                                    raise Exception(operation)

		self.inspectedItemsCount = 0

	def __repr__(self):
		return "Items: "+', '.join(map(str, self.items))

	def makeTurn(self, monkeys, isPart2=False, moduloValue=None):
		for item in self.items:
			item = self.operation(item)
			if isPart2 == False:
				item = int(item / 3)
			else:
				item%= moduloValue

			toMonkey = self.ifDivisibleThrowTo if item % self.testDivisor == 0 else self.ifNotDivisibleThrowTo
			monkeys[toMonkey].items.append(item)
			self.inspectedItemsCount+=1
		self.items = []

def solve(filename, isPart2=False):
	monkeys = {}
	inpt = open(filename, 'r').read().split("\n\n")

	for p in inpt:
		data = re.search('Monkey ([0-9]+):\s+Starting items: ([0-9, ]+)\s+Operation: (.+)\n\s+Test: divisible by ([0-9]+)\s+If true: throw to monkey ([0-9]+)\s+If false: throw to monkey ([0-9]+)', p).groups()
		monkeys[int(data[0])] = Monkey(list(map(int, data[1].split(", "))), data[2], int(data[3]), int(data[4]), int(data[5]))

	if not isPart2:
		for roundNumber in range(20):
			for monkeyNumber in monkeys:
				monkeys[monkeyNumber].makeTurn(monkeys)

	else: # Part 2
		moduloValue = 1
		for monkeyNumber in monkeys:
			moduloValue*=monkeys[monkeyNumber].testDivisor

		for roundNumber in range(10000):
			for monkeyNumber in monkeys:
				monkeys[monkeyNumber].makeTurn(monkeys, isPart2, moduloValue)

	monkeyActivity = []
	for monkeyNumber in monkeys:
		monkeyActivity.append(monkeys[monkeyNumber].inspectedItemsCount)

	monkeyActivity.sort(reverse=True)
	result = monkeyActivity[0] * monkeyActivity[1]

	print("Result of %s (part %d): %d" % (filename, 2 if isPart2 else 1, result))
	return result

assert solve('input/11.input.test') == 10605
assert solve('input/11.input') == 50616

assert solve('input/11.input.test', isPart2=True) == 2713310158
assert solve('input/11.input', isPart2=True) == 11309046332
