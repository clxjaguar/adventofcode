# cLx 2020 day 6

def check1(D):
	l = len(D)
	return(l)

def solve1(filename):
	fd = open(filename, 'r');

	cnt=0
	D = set()
	for line in fd:
		line = line.strip()
		if line == "":
			cnt += check1(D)
			D = set()
		else:
			for c in line:
				D.add(c)
	cnt += check1(D)
	return cnt

def check2(D, p):
	r = 0
	for i in D:
		if D[i] == p:
			r+=1
	return(r)

def solve2(filename):
	fd = open(filename, 'r');

	cnt=0
	D = {}; p=0
	for line in fd:
		line = line.strip()
		if line == "":
			cnt += check2(D, p)
			D = {}; p=0
		else:
			p+=1
			for c in line:
				if c in D:
					D[c]+= 1
				else:
					D[c] = 1
	cnt += check2(D, p)
	return cnt

print(solve1("input/6.input"))
print(solve2("input/6.input"))
