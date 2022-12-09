# cLx 2022 day 9

class Knot():
	def __init__(self, length, order=0, previous=None):
		self.x = 0
		self.y = 0
		self.order = order
		self.previous = previous
		if length > 1:
			self.next = Knot(length-1, self.order+1, self)
		else:
			self.next = None

	def __str__(self):
		return "Knot %d at position (%d, %d)" % (self.order, self.x, self.y)

	def __iter__(self):
		self.p = self
		return self

	def getChr(self):
		if self.order == 0:
			return 'H'
		if not self.next:
			return 'T'
		return str(self.order)

	def __next__(self):
		r = self.p
		if not r:
			raise StopIteration
		self.p = self.p.next
		return r

	def getTail(self):
		if self.next:
			return self.next.getTail()
		return self

	def getPosition(self):
		return (self.x, self.y)

	def moveUp(self):
		self.y+=1
		if self.next:
			self.next.update()

	def moveDown(self):
		self.y-=1
		if self.next:
			self.next.update()

	def moveLeft(self):
		self.x-=1
		if self.next:
			self.next.update()

	def moveRight(self):
		self.x+=1
		if self.next:
			self.next.update()

	def update(self):
		dx = self.x - self.previous.x
		dy = self.y - self.previous.y

		def minusAbsOne(val):
			if val<0: return val+1
			else: return val-1
		def sign(val):
			if val<0: return -1
			elif val>0: return 1
			else: return 0

		if abs(dx)>1 and abs(dy)>1:
			self.x-= sign(dx)
			self.y-= sign(dy)
			if self.next:
				self.next.update()

		# part 1
		elif self.x - self.previous.x > 1:
			self.x-=1
			self.y=self.previous.y
		elif self.x - self.previous.x <-1:
			self.x+=1
			self.y=self.previous.y
		elif self.y - self.previous.y > 1:
			self.y-=1
			self.x=self.previous.x
		elif self.y - self.previous.y <-1:
			self.y+=1
			self.x=self.previous.x
		else:
			return

		if self.next:
			self.next.update()

def printField(ropeHead, reset=False):
	global min_x, min_y, max_x, max_y
	if reset:
		min_x=0; min_y=0; max_x=6; max_y=5
	min_x, max_x = min(min_x, ropeHead.x), max(max_x, ropeHead.x)
	min_y, max_y = min(min_y, ropeHead.y), max(max_y, ropeHead.y)

	for y in range(max_y-1, min_y-1, -1):
		line = ['.']*(max_x-min_x)

		for knot in ropeHead:
			if knot.y != y: continue
			if knot.x<min_x: break

			if knot == '0': knot = 'H'
			if knot.x-min_x >= 0 and knot.x-min_x<len(line) and line[knot.x-min_x] == '.':
				line[knot.x-min_x] = knot.getChr()

		if line[0-min_x] == '.' and y == 0:
			line[0-min_x] = 'S'
		print(''.join(line))
	print()

def solve(filename, knots=2, debug=False):
	fd = open(filename, 'r')
	ropeHead = Knot(knots)
	ropeTailPositions = set()

	if debug:
		printField(ropeHead, reset=True)

	for line in fd:
		direction, steps = line.strip().split()
		if debug:
			print('==', direction, steps, '==')

		for _ in range(int(steps)):
			if    direction == 'R': ropeHead.moveRight()
			elif  direction == 'U': ropeHead.moveUp()
			elif  direction == 'L': ropeHead.moveLeft()
			elif  direction == 'D': ropeHead.moveDown()
			else: raise Exception(d)

			ropeTailPositions.add(ropeHead.getTail().getPosition())

			if debug:
				printField(ropeHead)

	result = len(ropeTailPositions)
	print("%s with %d knots: %d" % (filename, knots, result))
	return result

assert solve('input/9.input.test', debug=True) == 13
assert solve('input/9.input') == 6030

assert solve('input/9.input.test', knots=10) == 1
assert solve('input/9.input.test2', knots=10) == 36
assert solve('input/9.input', knots=10)
