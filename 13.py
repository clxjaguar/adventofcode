import time

def start():
	global startTime
	startTime = time.time()

def stop():
	global startTime
	return (time.time() - startTime) * 1000

# part 1
def solve1(earliest, busesInput):
	buses = []
	for bus in busesInput.split(","):
		if bus == 'x': continue
		buses.append(int(bus))

	start()
	t = earliest
	while True:
		for bus in buses:
			if t%bus == 0:
				result = (t-earliest)*bus
				print("\n", earliest, "\n", busesInput, "\n   =>", result, "(%fms)"%stop())
				return (t-earliest)*bus
		t+=1

assert solve1(939, "7,13,x,x,59,x,31,19") == 295
assert solve1(1002392, "23,x,x,x,x,x,x,x,x,x,x,x,x,41,x,x,x,37,x,x,x,x,x,421,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,17,x,19,x,x,x,x,x,x,x,x,x,29,x,487,x,x,x,x,x,x,x,x,x,x,x,x,13") == 3789

# part 2
def solve2(busesInput):
	# buses is a dictionnary containing departure offsets for each bus
	busesOffsets = {}
	for dt, bus in enumerate(busesInput.split(",")):
		if bus == 'x': continue
		busesOffsets[int(bus)] = dt

	start()

	# we make a sorted list of the buses
	busesSortedList = list(busesOffsets)
	busesSortedList.sort(reverse=True)

	# as we well start increment with the time with the greatest bus number, we can remove that bus from the list
	bus = busesSortedList.pop(0)
	t = bus-busesOffsets[bus];
	inc = bus

	# and we just have to find anothers
	while busesSortedList:
		bus = busesSortedList[0]
		if (busesOffsets[bus] + t) % bus:
			t+=inc;
		else:
			inc*=busesSortedList.pop(0)

	print("\n", busesInput, "\n   =>", t, "(%fms)"%stop())
	return t

#   T  G  M  k  1
# 100000000000000 la répones minimum selon énoncé (outch)
# 871100667227947 max d'itérations possibles (le produit des numéro des bus)
#     93055118897 ce que je peux tester en une minute (en incrémentant de numéro de bus le plus élevé)
# 667437230788118 la réponse à mon problème ... brute force is futile!

assert solve2("7,13,x,x,59,x,31,19") == 1068781
# others examples are:
#   assert solve2("17,x,13,19") == 3417
#   assert solve2("67,7,59,61") == 754018
#   assert solve2("67,x,7,59,61") == 779210
#   assert solve2("67,7,x,59,61") == 1261476
#   assert solve2("1789,37,47,1889") == 1202161486

# what we seek:
assert solve2("23,x,x,x,x,x,x,x,x,x,x,x,x,41,x,x,x,37,x,x,x,x,x,421,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,17,x,19,x,x,x,x,x,x,x,x,x,29,x,487,x,x,x,x,x,x,x,x,x,x,x,x,13") == 667437230788118
