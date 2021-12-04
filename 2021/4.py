# cLx 2021 day 4
import time

class BingoCard():
	def __init__(self):
		self.cells = {}
		self.y = 0
		self.size_x, self.size_y = (5, 5)
		self.won = False

	def loadLine(self, values):
		for x, value in enumerate(values):
			self.cells[(x, self.y)] = [value, False]
		self.y+=1

	def __repr__(self):
		res = "\n"
		for y in range(0, self.size_y):
			for x in range(0, self.size_x):
				c = "*" if self.cells[x, y][1] else " "
				res+= "%3d%s " % (self.cells[x, y][0], c)
			res+="\n"
		return res

	def checkNumber(self, number):
		r = False
		for y in range(0, self.size_y):
			for x in range(0, self.size_x):
				if self.cells[x, y][0] == number:
					if self.tickCoords(x, y):
						r = True
		return r

	def tickCoords(self, x, y):
		self.cells[x, y][1] = True

		r = True
		for y2 in range(0, self.size_y):
			if not self.cells[x, y2][1]:
				r = False
				break
		if r:
			self.won = True
			return True

		r = True
		for x2 in range(0, self.size_x):
			if not self.cells[x2, y][1]:
				r = False
				break
		if r:
			self.won = True
			return True

	def sumOfUntickNumbers(self):
		s = 0
		for y in range(0, self.size_y):
			for x in range(0, self.size_x):
				if not self.cells[x, y][1]:
					s+=self.cells[x, y][0]
		return s

def solve(filename, stopWhenWeWin=True):
	fd = open(filename, 'r')

	numberDrawns = tuple(map(int, fd.readline().strip().split(",")))

	cards = []

	print(numberDrawns)
	for line in fd:
		if len(line) <= 2:
			cards.append(BingoCard())
			continue

		lineValues = list(map(int, line.strip().split()))
		print(lineValues)
		cards[-1].loadLine(lineValues)

	for number in numberDrawns:
		# ~ print(number)
		for card in cards:
			if card.won:
				continue
			r = card.checkNumber(number)
			if r:
				s = card.sumOfUntickNumbers()
				result = s * number

				print(card)
				print(s, "x", number, "=", result)

				if stopWhenWeWin:
					return result

	return result

assert solve('input/4.input.test') == 4512
assert solve('input/4.input') == 45031

assert solve('input/4.input.test', stopWhenWeWin=False) == 1924
assert solve('input/4.input', stopWhenWeWin=False) == 2568
