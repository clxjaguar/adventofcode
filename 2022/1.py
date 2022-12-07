# cLx 2022 day 1

def solve1(filename):
	fd = open(filename, 'r')
	calsList = [0]

	for line in fd:
		line = line.strip()
		if not line:
			calsList.append(0)
		else:
			calsList[-1]+=int(line)

	result = max(calsList)
	print(result)
	return result


def solve2(filename):
	fd = open(filename, 'r')
	calsList = [0]

	for line in fd:
		line = line.strip()
		if not line:
			calsList.append(0)
		else:
			calsList[-1]+=int(line)

	calsList.sort(reverse=True)
	result = calsList[0] + calsList[1] + calsList[2]
	print(result)
	return result

assert solve1('input/1.input.test') == 24000
assert solve1('input/1.input') == 66186
assert solve2('input/1.input.test') == 45000
assert solve2('input/1.input') == 196804
