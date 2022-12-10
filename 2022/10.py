# cLx 2022 day 10

from itertools import count

def solve(filename, assertPart1=None, assertPart2=None):
	fd = open(filename, 'r')

	part1 = 0; part2 = ""
	x_reg = 1; remainingCycles = 0
	for clk in count(1):
		if remainingCycles:
			remainingCycles-=1
		else:
			instruction = fd.readline().strip().split()
			if not instruction:
				break
			if instruction[0] == 'addx':
				remainingCycles=1

		# Part 1
		if clk % 40 == 20:
			part1+=(clk*x_reg)

		# Part 2
		hpos = (clk - 1) % 40
		if part2 and hpos==0:    part2+='\n'
		if abs(x_reg - hpos)<=1: part2+='#'
		else:                    part2+='.'

		if remainingCycles==0:
			if instruction[0] == 'noop':
				pass # we are doing absolutely nothing!

			elif instruction[0] == 'addx':
				x_reg+=int(instruction[1])

			else:
				raise Exception(instruction[0])


	print("Part 1 of %s:" % filename, part1)
	if assertPart1 != None:
		assert part1 == assertPart1

	print("Part 1 of %s:\n%s" % (filename, part2))
	if assertPart2 != None:
		assert part2 == assertPart2


part2_test_result='\n'.join(["##..##..##..##..##..##..##..##..##..##..",
                             "###...###...###...###...###...###...###.",
                             "####....####....####....####....####....",
                             "#####.....#####.....#####.....#####.....",
                             "######......######......######......####",
                             "#######.......#######.......#######....."])

solve('input/10.input.test', assertPart1=13140, assertPart2=part2_test_result)
solve('input/10.input',      assertPart1=12840)
