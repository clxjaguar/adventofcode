# cLx 2021 day 8

def solve1(filename):
	fd = open(filename, 'r')

	counter = 0
	for line in fd:
		signal_patterns, digits_output = [el.strip().split() for el in line.split('|')]
		for digit in digits_output:
			if len(digit) in [2, 4, 3, 7]: # 1, 4, 7, 8
				counter+=1
	print(filename, counter)
	return counter

def solve2(filename):
	fd = open(filename, 'r')

	result = 0
	for line in fd:
		signal_patterns, digits_output = [el.strip().split() for el in line.split('|')]
		print(", ".join(signal_patterns), "=>", ", ".join(digits_output))

		segments_count = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0}
		segments2realSegmentsPossibles = {}
		for segment in segments_count:
			segments2realSegmentsPossibles[segment] = {'a':True, 'b':True, 'c':True, 'd':True, 'e':True, 'f':True, 'g':True}

		for signal_pattern in signal_patterns:
			l = len(signal_pattern)
			for segment in signal_pattern:
				segments_count[segment]+=1

				if l == 2:   # 1 => c, f
					segments2realSegmentsPossibles[segment]['a'] = False
					segments2realSegmentsPossibles[segment]['b'] = False
					segments2realSegmentsPossibles[segment]['d'] = False
					segments2realSegmentsPossibles[segment]['e'] = False
					segments2realSegmentsPossibles[segment]['g'] = False
				elif l == 4: # 4 => b, c, d, f
					segments2realSegmentsPossibles[segment]['a'] = False
					segments2realSegmentsPossibles[segment]['e'] = False
					segments2realSegmentsPossibles[segment]['g'] = False
				elif l == 3: # 7 => a, c, f
					segments2realSegmentsPossibles[segment]['b'] = False
					segments2realSegmentsPossibles[segment]['d'] = False
					segments2realSegmentsPossibles[segment]['e'] = False
					segments2realSegmentsPossibles[segment]['g'] = False

		segments2realsegment = {}
		contFlag = True
		while(contFlag):
			contFlag = False
			# a=8, b=6, c=8, d=7, e=4, f=9, g=7
			for segment, count in segments_count.items():
				# ~ print(segment, count, segments2realSegmentsPossibles[segment])
				if count == 4:
					segments2realsegment[segment] = 'e'
				elif count == 6:
					segments2realsegment[segment] = 'b'
				elif count == 7:
					if    segments2realSegmentsPossibles[segment]['d'] and not segments2realSegmentsPossibles[segment]['g']: segments2realsegment[segment] = 'd'
					elif  segments2realSegmentsPossibles[segment]['g'] and not segments2realSegmentsPossibles[segment]['d']: segments2realsegment[segment] = 'g'
				elif count == 8:
					if    segments2realSegmentsPossibles[segment]['a'] and not segments2realSegmentsPossibles[segment]['c']: segments2realsegment[segment] = 'a'
					elif  segments2realSegmentsPossibles[segment]['c'] and not segments2realSegmentsPossibles[segment]['a']: segments2realsegment[segment] = 'c'
				elif count == 9:
					segments2realsegment[segment] = 'f'

				try:
					# ~ print(segment, '=>', segments2realsegment[segment])
					for seg2, isPossible in segments2realSegmentsPossibles.items():
						if seg2 != segment and isPossible:
							segments2realSegmentsPossibles[seg2][segments2realsegment[segment]] = False
				except KeyError:
					contFlag = True

		print(segments2realsegment)

		realDigitsList = [set("abcefg"), set("cf"), set("acdeg"), set("acdfg"), set("bcdf"), set("abdfg"), set("abdefg"), set("acf"), set("abcdefg"), set("abcdfg")]
		digitValue = 0
		for digit in digits_output:
			digitValue*=10
			realDigit = set()
			for segment in digit:
				realDigit.add(segments2realsegment[segment])
			digitValue+=realDigitsList.index(realDigit)
		print(digitValue, "\n")
		result+=digitValue
	print(filename, result)
	return result

assert solve1('input/8.input.test') == 26
assert solve1('input/8.input') == 514

assert solve2('input/8.input.test') == 61229
assert solve2('input/8.input') == 1012272
