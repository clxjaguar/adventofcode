# cLx 2020 day 5

def decode(inp, verbose=False):
	inp = inp.replace("F", "0").replace("B", "1")
	inp = inp.replace("L", "0").replace("R", "1")
	id = int(inp, 2)

	if verbose:
		print("%s %3d" % (inp, id))

	return id

def solve(filename):
	fd = open(filename, 'r');

	ids = []
	for line in fd:
		line = line.strip()
		id = decode(line)
		ids.append(id)

	# part 1
	print(filename, "maximum id: %d" % max(ids))

	# part 2
	for id in range(max(ids)):
		if (id-1 in ids) and (id+1 in ids) and (not (id in ids)):
			print(filename, "missing id: %d" % id)

assert decode("FBFBBFFRLR", verbose=True) == 357 # row  44, column 5, seat ID 357
assert decode("BFFFBBFRRR", verbose=True) == 567 # row  70, column 7, seat ID 567.
assert decode("FFFBBBFRRR", verbose=True) == 119 # row  14, column 7, seat ID 119.
assert decode("BBFFBBFRLL", verbose=True) == 820 # row 102, column 4, seat ID 820.

solve('input/5.input')
