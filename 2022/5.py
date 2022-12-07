# cLx 2022 day 5

def solve(filename, crateMoverModel=9000):
	fd = open(filename, 'r')

	headers = []
	while True:
		line = fd.readline()
		if not line.strip():
			break

		headers.append(line.replace("\n", ""))

	maxi = max(map(int, headers[-1].split()))
	del headers[-1]

	crates = {}
	while headers:
		line = headers[-1]
		for i in range(1, maxi+1):
			try:               c = line[i*4-3]
			except IndexError: break
			if c != ' ':
				if i not in crates: crates[i] = []
				crates[i].append(c)
		del headers[-1]

	for line in fd:
		d = line.strip().split()
		quantity, originStack, destinationStack = int(d[1]), int(d[3]), int(d[5])

		if crateMoverModel == 9000:
			for i in range(quantity):
				crates[destinationStack].append(crates[originStack].pop())
		elif crateMoverModel == 9001:
			crates[destinationStack]+= crates[originStack][-quantity:]
			crates[originStack] = crates[originStack][0:-quantity]

	result = ""
	for i in crates.keys():
		result+=crates[i][-1]

	print(result)
	return result

assert solve('input/5.input.test') == "CMZ"
assert solve('input/5.input')

assert solve('input/5.input.test', crateMoverModel=9001) == "MCD"
assert solve('input/5.input',      crateMoverModel=9001) == "MGDMPSZTM"
