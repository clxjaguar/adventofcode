# cLx 2022 day 13

def compare(left, right, level=0):
	# ~ print('%sCompare %s vs %s' % ('  '*level, left, right))
	if type(left) is int and type(right) is int:
		if left < right:
			return 1
		if left > right:
			return -1
		else:
			return 0

	if type(left)  is int: left  = [left]
	if type(right) is int: right = [right]

	for l, r in zip(left, right):
		r = compare(l, r, level+1)
		if r: return r

	if len(left) < len(right):
		return 1
	if len(left) > len(right):
		return -1

class Packet():
	def __init__(self, value):
		if type(value) == str:
			self.value = eval(value) # never do that, please
		else:
			self.value = value

	def __repr__(self):
		return str(self.value)

	def __lt__(self, x):
		return True if compare(x.value, self.value) == -1 else False

	def __gt__(self, x):
		return True if compare(x.value, self.value) ==  1 else False

def solve1(filename):
	inpt = open(filename, 'r').read().split("\n\n")

	result = 0
	for i, packetPairStr in enumerate(inpt, start=1):
		print("== Pair %d ==" % i)
		left, right = map(Packet, packetPairStr.strip().split('\n'))

		if not left > right:
			print("Inputs are in the right order")
			result+=i
		else:
			print("Inputs are NOT in the right order")
		print()

	print("%s (part 1): %d" % (filename, result))
	return result

def solve2(filename):
	packets = list(map(Packet, open(filename, 'r').read().replace("\n\n", "\n").strip().split('\n')))
	packets.append(Packet([[2]]))
	packets.append(Packet([[6]]))

	packets = sorted(packets)

	result = 1
	for i, packet in enumerate(packets, start=1):
		if packet.value in ([[2]], [[6]]):
			result*=i

	print("%s (part 2): %d" % (filename, result))
	return result

assert solve1('input/13.input.test') == 13
assert solve1('input/13.input') == 5366

assert solve2('input/13.input.test') == 140
assert solve2('input/13.input') == 23391

assert solve1('input/13.input2') == 6086
assert solve2('input/13.input2') == 27930
