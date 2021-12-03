# cLx 2021 day 3

def count_bits(bit, inpt):
	bits_one, bits_zero = (0, 0)

	for line in inpt:
		bitVal = line[-bit-1]
		if bitVal == "1":   bits_one+=1
		elif bitVal == "0": bits_zero+=1

	return bits_one, bits_zero

def solve1(filename):
	inpt = open(filename, 'r').read().split()

	gamma, epsilon = (0, 0)
	for bit in range(len(inpt[0])):
		bits_one, bits_zero = count_bits(bit, inpt)
		if bits_one > bits_zero: gamma+=2**bit
		else: epsilon+=2**bit

	result = gamma * epsilon
	print(gamma, "x", epsilon, "=", result)
	return result

def solve2(filename):
	inpt = open(filename, 'r').read().split()

	def algo(fkeep):
		inpt2 = inpt.copy();
		for bit in reversed(range(len(inpt[0]))):
			bits_one, bits_zero = count_bits(bit, inpt2)
			keep = fkeep(bits_one, bits_zero)

			idx = 0
			while idx < len(inpt2):
				if inpt2[idx][-bit-1] == keep: idx+=1
				else: del inpt2[idx]

			if len(inpt2) == 1: return int(inpt2[0], 2)

	oxygen_generator_rating = algo(lambda ones, zeros: "0" if ones < zeros else "1")
	CO2_scrubber_rating = algo(lambda ones, zeros: "1" if ones < zeros else "0")

	result = oxygen_generator_rating * CO2_scrubber_rating
	print(oxygen_generator_rating, "x", CO2_scrubber_rating, "=", result)
	return result


assert solve1('input/3.input.test') == 198
assert solve1('input/3.input') == 841526
assert solve2('input/3.input.test') == 230
assert solve2('input/3.input') == 4790390
