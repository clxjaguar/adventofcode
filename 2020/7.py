# cLx 2020 day 7

import re

def indent(level):
	return " "*level*4

def checkBag(bagToCheck, bags, bagsPossibles, level=0):
	global maxLevel; maxLevel=max(maxLevel, level)

	if level == 0:
		print("\n%s# %s" % (indent(level), bagToCheck))
	else:
		bagsPossibles.add(bagToCheck)

	for bagOutside in bags:
		for nbrOf, bagInside in bags[bagOutside]:
			if bagInside == bagToCheck:
				print("%s* %s" % (indent(level+1), bagOutside))
				bagsPossibles.add(bagOutside)
				checkBag(bagOutside, bags, bagsPossibles, level+1)

def countBags(bagToCheck, bags, level=0):
	global maxLevel; maxLevel=max(maxLevel, level)

	if level == 0:
		print("\n%s# %s" % (indent(level), bagToCheck))
		counter = 0
	else:
		counter = 1

	for nbrOf, bagInside in bags[bagToCheck]:
		numberOfBagsInside = int(nbrOf)
		print("%s* %s x %d" % (indent(level+1), bagInside, numberOfBagsInside))
		counter+= numberOfBagsInside * countBags(bagInside, bags, level+1)

	if counter != 1:
		print(indent(level), counter)

	return counter

def solve(filename, assertPart1=None, assertPart2=None):
	global maxLevel
	bags = {}
	fd = open(filename, 'r')

	for line in fd:
		line = line.strip()
		if not line: continue
		match = re.match("^([a-z ]+) bags contain (.+)$", line)
		bagName = match.group(1)
		submatch = re.findall("([0-9]+) ([a-z ]+) bag", match.group(2))
		bags[bagName] = submatch

	print(bags)
	maxLevel = 0
	bagsPossibles = set()
	checkBag("shiny gold", bags, bagsPossibles)
	print(filename, "part 1: %d possible containers bags (max levels: %d)" % (len(bagsPossibles), maxLevel+1))
	print("        %s\n" % bagsPossibles)
	if assertPart1 != None:
		assert len(bagsPossibles) == assertPart1

	maxLevel = 0
	bagsCount = countBags("shiny gold", bags)
	print(filename, "part 2: %d bags inside root bag (max levels: %d)" % (bagsCount, maxLevel+1))
	if assertPart2 != None:
		assert bagsCount == assertPart2

solve("input/7.input.test", 4, 32)
solve("input/7.input", 278, 45157)
