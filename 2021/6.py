# cLx 2021 day 6

from collections import defaultdict

def solve(filename, days):
	inpt = map(int, open(filename, 'r').read().strip().split(','))
	lanternFishes = defaultdict(int)
	for timer in inpt:
		lanternFishes[timer]+=1

	for day in range(days):
		lanternFishesNextDay = defaultdict(int)
		for timer, number in lanternFishes.items():
			if timer > 0:
				lanternFishesNextDay[timer-1]+= number
			else:
				lanternFishesNextDay[6]+= number
				lanternFishesNextDay[8] = number
		lanternFishes = lanternFishesNextDay
	result = sum(lanternFishes.values())

	print("%s: %d fish after %d days" % (filename, result, days))
	return(result)

assert solve('input/6.input.test', days=18)  ==            26
assert solve('input/6.input.test', days=80)  ==          5934
assert solve('input/6.input',      days=80)  ==        360761
assert solve('input/6.input.test', days=256) ==   26984457539
assert solve('input/6.input',      days=256) == 1632779838045
