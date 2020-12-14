# cLx 2020 day 10

def traverseJolts(joltageMap, joltageNow, joltToFind, voltageToCombinations, level=0, counter=0):
	if joltageNow in voltageToCombinations:
		print(" "*level, voltageToCombinations[joltageNow], joltageNow)
		return voltageToCombinations[joltageNow]

	if joltageNow == joltToFind:
		print(" "*level, counter+1, joltageNow)
		return counter+1

	for outputJoltage in joltageMap[joltageNow]:
		counter+=traverseJolts(joltageMap, outputJoltage, joltToFind, voltageToCombinations, level+1)

	voltageToCombinations[joltageNow] = counter
	print(" "*level, counter, joltageNow)
	return counter

def solve(filename):
	print("***", filename)
	A = open(filename, 'r').read().split("\n")

	adapterOutputJolts = []
	for val in A:
		if val:
			adapterOutputJolts.append(int(val))

	# Any given adapter can take an input 1, 2, or 3 jolts lower than its rating and still produce its rated output joltage.

	deviceJoltage = max(adapterOutputJolts)+3
	print(deviceJoltage, adapterOutputJolts)

	joltageMap = {} # input joltage => output joltage
	for outputAdapterJoltage in adapterOutputJolts:
		for i in range(1, 4):
			if (outputAdapterJoltage-i) not in joltageMap:
				joltageMap[outputAdapterJoltage-i] = []
			joltageMap[outputAdapterJoltage-i].append(outputAdapterJoltage)


	joltageNow = 0
	remainingAdapters = adapterOutputJolts.copy()
	remainingAdapters.append(deviceJoltage)
	diffscounts = {}; diffscounts[1] = 0; diffscounts[2] = 0; diffscounts[3] = 0
	while(len(remainingAdapters) != 0):
		adapOutputJoltage = min(remainingAdapters)
		diffscounts[adapOutputJoltage - joltageNow]+=1
		joltageNow = adapOutputJoltage
		remainingAdapters.remove(adapOutputJoltage)

	# part 1
	answerPart1 = diffscounts[1]*diffscounts[3]
	print("Part 1:", answerPart1)

	# part 2
	answerPart2 = traverseJolts(joltageMap, joltageNow=0, joltToFind=deviceJoltage-3, voltageToCombinations={})
	print("Part 2:", answerPart2)
	return (answerPart1, answerPart2)

assert solve("input/10.input.test")  == (7*5, 8)
assert solve("input/10.input.test2") == (22*10, 19208)
assert solve("input/10.input")       == (2475, 442136281481216)
