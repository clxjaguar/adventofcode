# cLx 2020 day 16

def loadPuzzleInput(filename):
	fd = open(filename, 'r')

	rules = {}
	for line in fd:
		line = line.strip()
		if line == "":
			continue
		if line == "your ticket:":
			break
		data = line.split(": ", 1)
		rules[data[0]] = tuple((int(rng.split('-')[0]),int(rng.split('-')[1])) for rng in (data[1].split(" or ")))

	for line in fd:
		line = line.strip()
		if line == "":
			continue
		if line == "nearby tickets:":
			break
		myTicket = tuple(int(v) for v in line.split(','))

	tickets = []
	for line in fd:
		line = line.strip()
		if line == "":
			continue
		tickets.append(tuple(map(int, line.split(","))))

	return rules, tickets, myTicket

def validate(value, rules, ruleName):
	ranges = rules[ruleName]
	for rng in ranges:
		if value >= rng[0] and value <= rng[1]:
			return True
	return False

def tryToValidateAllValues(values, rules):
	invalidValuesSum = 0
	ticketIsValid = True

	for value in values:
		ok = False
		for ruleName in rules:
			# each value should pass AT LEAST one rule, not all of them
			if validate(value, rules, ruleName):
				ok = True
				break

		if not ok:
			assert invalidValuesSum == 0 # only one bad value in one ticket
			invalidValuesSum+=value
			ticketIsValid = False

	return invalidValuesSum, ticketIsValid

def solve(filename, assertPart1=None, assertPart2=None):
	rules, tickets, myTicket = loadPuzzleInput(filename)

	ticketScanningErrorRate = 0
	validTickets = []
	for ticketValues in tickets:
		invalidValuesSum, ticketIsValid = tryToValidateAllValues(ticketValues, rules)
		if ticketIsValid:
			validTickets.append(ticketValues)
		else:
			ticketScanningErrorRate+=invalidValuesSum

	### part 1
	print("ticketScanningErrorRate=%d" % (ticketScanningErrorRate))
	if assertPart1 != None:
		assert ticketScanningErrorRate == assertPart1

	### part 2
	fieldCount = len(myTicket)

	fieldsPositionPossibles = {}
	for ruleName in rules:
		fieldsPositionPossibles[ruleName] = set()

	for i in range(fieldCount):
		for ruleName in rules:
			fieldsPositionPossibles[ruleName].add(i)

	for fieldName in rules:
		fieldPositionPossibles = fieldsPositionPossibles[fieldName].copy()
		for fieldPosition in fieldsPositionPossibles[fieldName]:
			for ticket in validTickets:
				if not validate(ticket[fieldPosition], rules, fieldName):
					fieldPositionPossibles.remove(fieldPosition)
					break
		fieldsPositionPossibles[fieldName] = fieldPositionPossibles

	print("fieldsPositionPossibles:", fieldsPositionPossibles)

	continueLoop = True
	fieldsPosition = {}
	while continueLoop:
		continueLoop = False
		for fieldName in fieldsPositionPossibles:
			if type(fieldsPositionPossibles[fieldName]) == int:
				continue
			if len(fieldsPositionPossibles[fieldName]) == 1:
				continueLoop = True
				fieldValue = list(fieldsPositionPossibles[fieldName])[0]
				for fieldNameToDeletePosition in fieldsPositionPossibles:
					if type(fieldsPositionPossibles[fieldNameToDeletePosition]) == int:
						continue
					if fieldValue in fieldsPositionPossibles[fieldNameToDeletePosition]:
						fieldsPositionPossibles[fieldNameToDeletePosition].remove(fieldValue)
				fieldsPosition[fieldName] = fieldValue
				break

	print("fieldsPosition:")
	for fieldName in fieldsPosition:
		pos = fieldsPosition[fieldName]
		print(fieldName+":", pos, "("+str(myTicket[pos])+")")

	print("\nmyTicket:", myTicket)

	val = False; product = 1
	for fieldName in fieldsPosition:
		if fieldName.startswith("departure"):
			pos = fieldsPosition[fieldName]
			val = myTicket[pos]
			print(fieldName+":", val)
			product*=val

	if val != False:
		print("product:", product)

	if assertPart2 != None:
		assert product == assertPart2


solve("input/16.input.test", assertPart1=71)
solve("input/16.input.test2")
solve("input/16.input", assertPart1=23009, assertPart2=10458887314153)

