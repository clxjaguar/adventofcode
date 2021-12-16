# cLx 2021 day 16

from functools import reduce
import time

def parse(binary):
	global result1

	def take(n):
		t = []
		for b in range(n):
			t.append(binary.pop(0))
		# ~ print(t, binary)
		return t

	def toInt(bits):
		val = 0; p = 1
		while len(bits):
			val+= bits.pop() * p
			p<<=1
		return val

	packetVersion = toInt(take(3))
	# ~ print("packetVersion:", packetVersion)
	result1+=packetVersion
	typeID = toInt(take(3))
	if typeID == 4: # literal value
		contFlag = True
		binVal = []
		while(contFlag):
			contFlag = binary.pop(0)
			binVal+=take(4)

		literalValue = toInt(binVal)
		# ~ print("literal value:", literalValue)
		return literalValue

	else: # operator packet
		lengthTypeID = binary.pop(0)
		# ~ print("typeID:", typeID)
		if lengthTypeID == 0:
			subPacketsTotalLength = toInt(take(15))
			nbrOfSubPackets = None
			# ~ print("  subPacketsTotalLength:", subPacketsTotalLength)
		elif lengthTypeID == 1:
			nbrOfSubPackets = toInt(take(11))
			subPacketsTotalLength = None
			# ~ print("  nbrOfSubPackets:", nbrOfSubPackets)

		contents = []; initialLength = len(binary)
		while(True):
			contents.append(parse(binary))

			if nbrOfSubPackets       and len(contents) >= nbrOfSubPackets or \
			   subPacketsTotalLength and initialLength - len(binary) >= subPacketsTotalLength:
				break

		if typeID == 0: return sum(contents)
		if typeID == 1: return reduce(lambda x, y: x*y, contents)
		if typeID == 2: return min(contents)
		if typeID == 3: return max(contents)
		if typeID == 5: return 1 if contents[0] > contents[1] else 0
		if typeID == 6: return 1 if contents[0] < contents[1] else 0
		if typeID == 7: return 1 if contents[0] == contents[1] else 0
		raise ValueError("unknown typeID %d" % typeID)

def decode(hexString):
	global result1
	result1 = 0
	print("Decoding: ", hexString)
	binary = [int(c) for c in "".join([bin(int(c, 16)+32)[-4:] for c in hexString])]
	result2 = parse(binary)
	return result1, result2

def solve(filename, part2=False, refreshInterval=-1):
	inpt = open(filename, 'r').read().strip()
	start = time.time()
	result1, result2 = decode(inpt)
	print("%s: Part1=%d\tPart2=%d\t(%.2fms)" % (filename, result1, result2, (time.time()-start)*1000))
	return result1, result2

# tests for part 1
assert decode("8A004A801A8002F478")            [0] == 16
assert decode("620080001611562C8802118E34")    [0] == 12
assert decode("C0015000016115A2E0802F182340")  [0] == 23
assert decode("A0016C880162017C3686B18A3D4780")[0] == 31

# tests for part 2
assert decode("C200B40A82")                    [1] == 3
assert decode("04005AC33890")                  [1] == 54
assert decode("880086C3E88112")                [1] == 7
assert decode("CE00C43D881120")                [1] == 9
assert decode("F600BC2D8F")                    [1] == 0
assert decode("9C005AC2F8F0")                  [1] == 0
assert decode("9C0141080250320F1802104A08")    [1] == 1

# computing with real data
assert solve('input/16.input') == (977, 101501020883)
