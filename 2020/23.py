# cLx 2020 day 23

# The small crab challenges you to a game! The crab is going to mix up some
# cups, and you have to predict where they'll end up. The cups will be arranged
# in a circle and labeled clockwise (your puzzle input). For example, if your
# labeling were 32415, there would be five cups in the circle; going clockwise
# around the circle from the first cup, the cups would be labeled 3, 2, 4, 1, 5,
# and then back to 3 again.

class Cup():
	def __init__(self, label):
		self.label = label
		self.next = None

	def pickUpNextThree(self):
		pickedUp = self.next
		self.next = pickedUp.next.next.next
		pickedUp.next.next.next = None
		return pickedUp

	def insertPickedUp(self, pickedUp):
		pickedUp.next.next.next = self.next
		self.next = pickedUp

	def hashmap(self):
		s = set()
		s.add(self.label)
		next = self.next
		while(next != None and next != self):
			s.add(next.label)
			next = next.next
		return s

	def listCups(self, stopBeforeLabel=None):
		l = [self.label]
		next = self.next
		while(next != None and next.label != stopBeforeLabel):
			if next == self:
				break
			l.append(next.label)
			next = next.next
		return l

	def __repr__(self):
		s = str(self.label)
		next = self.next
		while(next != None):
			if next == self:
				s+="..."
				break
			s+=", "+str(next.label)
			next = next.next
		return s

def makeCups(labels, upTo):
	cups = []
	lastCup = None
	for label in labels:
		cup = Cup(label)
		cups.append(cup)
		if lastCup != None:
			lastCup.next = cup
		lastCup = cup

	if upTo: # part 2
		for i in range(max(labels) + 1, upTo+1):
			cup = Cup(i)
			cups.append(cup)
			lastCup.next = cup
			lastCup = cup
	lastCup.next = cups[0]

	label2cupIndexes = {}
	for cup in cups:
		label2cupIndexes[cup.label] = cup
	return cups, label2cupIndexes

import time

def solve(puzzleInput, movesToDo, part2numberOfCups=None):
	print("***", puzzleInput, "with", movesToDo, "moves ***")
	labels = tuple(int(c) for c in puzzleInput)
	cups, label2cupIndexes = makeCups(labels, upTo=part2numberOfCups)
	t = 0

	allCupsHashmap = cups[0].hashmap()
	minCupLabel = min(labels)
	maxCupLabel = max(allCupsHashmap)

	# Before the crab starts, it will designate the first cup in your list as the
	# current cup.

	currentCup = cups[0]

	# The crab is then going to do N moves.
	move = 0

	while move < movesToDo:
		# Each move, the crab does the following actions:

		# The crab picks up the three cups that are immediately clockwise of the current
		# cup. They are removed from the circle; cup spacing is adjusted as necessary to
		# maintain the circle.

		move+=1
		if not part2numberOfCups or time.time() > t:
			t = time.time() + 1
			print("-- move %d --" % move)

		pickedUpCups = currentCup.pickUpNextThree()
		if not part2numberOfCups:
			print("cups:", currentCup)
			print("pick up:", pickedUpCups)

		# The crab selects a destination cup: the cup with a label equal to the current
		# cup's label minus one.

		i = currentCup.label - 1

		# If this would select one of the cups that was just picked up, the crab will
		# keep subtracting one until it finds a cup that wasn't just picked up.

		while i in pickedUpCups.hashmap() or i < minCupLabel:
			i-=1

			# If at any point in this process the value goes below the lowest value on
			# any cup's label, it wraps around to the highest value on any cup's label
			# instead.

			if i < minCupLabel:
				i = maxCupLabel
		destinationCup = label2cupIndexes[i]
		if not part2numberOfCups:
			print("Destination:", i)
			print()

		# The crab places the cups it just picked up so that they are immediately
		# clockwise of the destination cup. They keep the same order as when they
		# were picked up.

		destinationCup.insertPickedUp(pickedUpCups)

		# The crab selects a new current cup: the cup which is immediately clockwise
		# of the current cup.

		currentCup = currentCup.next

	print("-- final --")
	if not part2numberOfCups: # part 1
		print("cups:", currentCup)
		part1answer = "".join(map(str, label2cupIndexes[1].next.listCups(stopBeforeLabel=1)))
		print(part1answer)
		print()
		return part1answer
	else: # part 2
		a = label2cupIndexes[1].next.label
		b = label2cupIndexes[1].next.next.label
		part1answer = a*b
		print(a, "*", b, "=", part1answer)
		print()
		return part1answer

puzzleInput = open("input/23.input").read().strip()

# part 1
assert solve("389125467", 10) == "92658374"
assert solve("389125467", 100) == "67384529"
assert solve("643719258", 100) == "54896723" # this was my part 1 problem

# part 2
assert solve("389125467", 10000000, 1000000) == 149245887792
assert solve("643719258", 10000000, 1000000) == 146304752384
