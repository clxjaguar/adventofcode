# cLx 2021 day 17

import sys, re

def simulate(velocity_x, velocity_y, target_x1, target_x2, target_y1, target_y2):
	x, y = (0, 0); max_y = 0
	while(x <= target_x2 and y >= target_y1):
		if y > max_y: max_y = y
		if target_x1 <= x <= target_x2 and target_y1 <= y <= target_y2:
			return max_y
		x+=velocity_x; y+=velocity_y
		if velocity_x > 0: velocity_x-=1
		elif velocity_x < 0: velocity_x+=1
		velocity_y-=1

def solve(filename):
	inpt = open(filename).read().strip()
	m = re.search('x=([0-9-]+)\.\.([0-9-]+), y=([0-9-]+)\.\.([0-9-]+)', inpt)
	target_x1, target_x2, target_y1, target_y2 = map(int, (m.group(1), m.group(2), m.group(3), m.group(4)))

	shoots = {}
	for velocity_y in range(target_y1-1, 1000):  # that is brute force, not
		for velocity_x in range(0, target_x2+1): # very elegant but does the work here...
			r = simulate(velocity_x, velocity_y, target_x1, target_x2, target_y1, target_y2)
			if r != None: shoots[(velocity_x, velocity_y)] = r

	result1 = max(shoots.values())
	result2 = len(shoots)
	print("%s, %s: \tPart 1: %d\tPart 2: %d" % (filename, inpt, result1, result2))
	return (result1, result2)

assert solve('input/17.input.test') == (45, 112)
assert solve('input/17.input') == (7626, 2032)

