# cLx 2020 day 19 (very messy version)

import re

def solve(filename, applyPatchPart2=False, patchIterLoop=10, showHowMessyWeAre=False):
	fd = open(filename)

	rules = {}
	for line in fd:
		line = line.strip()
		if line == "":
			break
		ruleNumber, rule = line.split(": ")
		rules[ruleNumber] = rule

	decodedRules = {}

	cont = True
	while cont:
		cont = False
		for ruleId in rules:
			rule=rules[ruleId]
			if ruleId not in decodedRules:
				if rule[0] == '"':
					if ruleId not in decodedRules:
						decodedRules[ruleId] = rule[1]
						cont = True
				else:
					ok = True
					l1 = []
					t1 = rule.split("|")
					for e1 in t1:
						t2 = e1.split()
						l2 = []
						for e2 in t2:
							if e2 in decodedRules:
								l2.append(decodedRules[e2])
							else:
								ok = False
						if ok:
							c2 = "".join(l2)
							l1.append(c2)
					if ok:
						c1 = "|".join(l1)
						decodedRules[ruleId] = '('+c1+')'
						cont = True

	puzzleLines = fd.read().split('\n')

	if not applyPatchPart2:
		# part 1
			r = re.compile('^'+decodedRules['0']+'$')
			count_pass = 0
			count_fail = 0
			for line in puzzleLines:
				if r.match(line):
					count_pass+=1
				else:
					count_fail+=1
			print("%-25s"%filename, "pass: ", count_pass, "\tfail: ", count_fail)

	else:
		# part 2 i'm so sorry
		rule8 = decodedRules['8']+'+'

		for messyDirtyNaughty in range(patchIterLoop):
			r = re.compile('^'+decodedRules['0']+'$')
			count_pass = 0
			count_fail = 0
			for line in puzzleLines:
				if r.match(line):
					count_pass+=1
				else:
					count_fail+=1
			print("%-25s"%filename, "pass: ", count_pass, "\tfail: ", count_fail, "\titer:", messyDirtyNaughty)

			decodedRules['8'] = rule8
			decodedRules['11'] = '('+decodedRules['42']+decodedRules['31']+'|'+decodedRules['42']+decodedRules['11']+decodedRules['31']+')'
			decodedRules['0'] = '('+decodedRules['8'] + decodedRules['11']+')'

	print()
	if showHowMessyWeAre:
		print('^'+decodedRules['0']+'$')

	return count_pass

# part 1
assert solve("input/19.input.test")                        == 2
assert solve("input/19.input")                             == 144

# part 2
assert solve("input/19.input.test2", applyPatchPart2=True) == 12
assert solve("input/19.input",       applyPatchPart2=True) == 260

# how dirty!
assert solve("input/19.input", applyPatchPart2=True, patchIterLoop=4, showHowMessyWeAre=True) == 260
