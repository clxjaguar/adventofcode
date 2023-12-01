# cLx 2023 day 1

def solve1(filename):
	total = 0
	for line in open(filename):
		line = line.strip()
		for c in line:
			if c.isdigit():
				f = c
				break

		for c in reversed(line):
			if c.isdigit():
				l = c
				break

		value = int(f+l)
		total += value
	print("Part 1 of %s:" % filename, total)
	return total

def solve2(filename):
	total = 0
	digits = {"one":1, "1":1,
			  "two":2, "2":2,
			  "three":3, "3":3,
			  "four":4, "4":4,
			  "five":5, "5":5,
			  "six":6, "6":6,
			  "seven":7, "7":7,
			  "eight":8, "8":8,
			  "nine":9, "9":9}

	for line in open(filename):
		line = line.strip()

		f, fp, l, lp = [None]*4
		for k,v in digits.items():
			p = line.find(k)
			if p>=0 and (fp is None or p<fp): fp=p; f=v
			p = line.rfind(k)
			if p>=0 and (lp is None or p>lp): lp=p; l=v

		value = 10*f + l
		total += value

	print("Part 2 of %s:" % filename, total)
	return total

assert solve1("input/1.input.test") == 142
assert solve1("input/1.input") == 55834
assert solve2("input/1.input.test2") == 281
assert solve2("input/1.input") == 53221
