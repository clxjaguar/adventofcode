# cLx 2020 day 9

def calculate(inp):
	possibilities = set()
	for i, iv in enumerate(inp):
		for jv in inp[i+1:]:
			possibilities.add(iv+jv)
	return possibilities

def solve(filename, preamble):
	fd = open(filename, 'r')

	# part 1
	data = []
	cnt=0
	for line in fd:
		line = line.strip()
		if line:
			val = int(line)
			if cnt>=preamble:
				possibilities = calculate(data[cnt-preamble:])
				if not val in possibilities:
					invalidNumber = val
					print("*** The invalid number is", invalidNumber)
					break
			data.append(val)
			cnt+=1

	# part 2
	for i, iv in enumerate(data):
		s = 0
		vals = set()
		for jv in data[i:]:
			s+=jv
			if s > invalidNumber: break # awwww...
			vals.add(jv)
			if s == invalidNumber:
				answer = min(vals)+max(vals)
				print("*** Found! From %d to %d, the answer is %d" % (iv, jv, answer))
				return (invalidNumber, answer)

assert solve("input/9.input.test", preamble=5)  == (127, 62)
assert solve("input/9.input",      preamble=25) == (3199139634, 438559930)

