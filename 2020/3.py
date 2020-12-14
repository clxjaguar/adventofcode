# cLx 2020 day 3

fd = open('input/3.input', 'r')

def ovwchar(line, pos, char):
	return(line[0:pos]+char+line[pos+len(char):])

def traverse(right, down, printmap=True):
	cnt=0
	hpos=0
	fd.seek(0)
	for line in fd:
		line = line.strip()
		hpos%=len(line)
		if line[hpos] == '#':
			cnt+=1; c='X'
		else:
			c='O'
		if printmap:
			line = ovwchar(line, hpos, c);
			print("%s %4d %4d" % (line, hpos, cnt))
		hpos+=right
		for _ in range(down-1):
			line = fd.readline().strip()
			if printmap:
				print(line)
	if printmap: print()
	print("Traversing map right %d down %d meet %d trees" % (right, down, cnt))
	if printmap: print()
	return cnt

# first part
traverse(3, 1)

# second part
product = traverse(1, 1, False)
product*= traverse(3, 1, False)
product*= traverse(5, 1, False)
product*= traverse(7, 1, False)
product*= traverse(1, 2, False)
print("The product of all these traversals is", product)
