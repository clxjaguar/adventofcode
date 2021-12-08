# cLx 2021 day 7

def solve(filename, checkCost):
	inpt = list(map(int, open(filename, 'r').read().strip().split(',')))

	pos = round(sum(inpt)/len(inpt))
	lastFuel = float('nan'); direction = 1
	while(True):
		fuel = checkCost(inpt, pos)
		if fuel > lastFuel:
			if direction == 1:
				direction*=-1
			else:
				print(lastFuel)
				return lastFuel
		pos+= direction; lastFuel = fuel

def checkCost1(inpt, target):
	fuel = 0
	for pos in inpt:
		fuel += abs(pos - target)
	return fuel

def checkCost2(inpt, target):
	fuel = 0
	for pos in inpt:
		delta = abs(pos - target)
		fuel += delta*(delta+1)/2
	return int(fuel)

assert solve('input/7.input.test', checkCost1) ==       37
assert solve('input/7.input',      checkCost1) ==   337833
assert solve('input/7.input.test', checkCost2) ==      168
assert solve('input/7.input',      checkCost2) == 96678050

