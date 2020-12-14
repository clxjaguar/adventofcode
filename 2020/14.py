# cLx 2020 day 14

import re

def solve1(filename):
	memory = {}
	fd = open(filename)
	for line in fd:
		line = line.strip()
		m = re.search("^mask = ([X01]{36})$", line)
		if m:
			mask = m.group(1)
			andMask = int(mask.replace("X", "1"), 2)
			orMask = int(mask.replace("X", "0"), 2)
		else:
			a = re.search("^mem\[([0-9]+)\] = ([0-9]+)$", line)
			address = int(a.group(1))
			value = int(a.group(2))

			maskedValue = (value & andMask) | orMask
			memory[address] = maskedValue

	summedValues = 0
	for value in memory.values():
		summedValues+=value

	print(filename, summedValues)
	return summedValues

def dec2bin(val, len):
	s = ""
	for i in range(len):
		s = ("1" if (val & (2**i)) else "0") + s
	return s

def solve2(filename):
	memory = {}
	fd = open(filename)
	for line in fd:
		line = line.strip()
		m = re.search("^mask = ([X01]{36})$", line)
		if m:
			mask = m.group(1)
		else:
			a = re.search("^mem\[([0-9]+)\] = ([0-9]+)$", line)
			address = int(a.group(1))
			value = int(a.group(2))

			addressBin = dec2bin(address, len(mask))
			for i in range(len(mask)):
				if mask[i] == "X":
					addressBin = addressBin[0:i] + "X" + addressBin[i+1:]
				elif mask[i] == "1":
					addressBin = addressBin[0:i] + "1" + addressBin[i+1:]

			adressesBin = [addressBin]
			for pos in range(len(mask)):
				if addressBin[pos] == 'X':
					newAdressesBin = []
					for A in adressesBin:
						newAdressesBin.append(A[:pos] + "0"+ A[pos+1:])
						newAdressesBin.append(A[:pos] + "1"+ A[pos+1:])
					adressesBin = newAdressesBin

			for addressBin in adressesBin:
				address = int(addressBin, 2)
				memory[address] = value

	summedValues = 0
	for value in memory.values():
		summedValues+=value

	print(filename, summedValues)
	return summedValues

# part 1
assert solve1("input/14.input.test") == 165
assert solve1("input/14.input") == 12408060320841

# part 2
assert solve2("input/14.input.test2") == 208
assert solve2("input/14.input") == 4466434626828
