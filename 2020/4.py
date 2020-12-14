# cLx 2020 day 4

import re

def valValueEx(D, pattern, field, debugField=False, checkLength=None):
	if field in D:
		if checkLength==None or len(D[field]) == checkLength:
			if re.match(pattern, D[field]):
				if debugField:
					print("%s passed: %s (%s)" % (field, D[field], pattern))
				return True

	if debugField or validTestDataSet:
		print(D)
		if not field in D:
			print("%s failed (not in set)" % (field))
		else:
			print("%s failed: %s (%s)" % (field, D[field], pattern))
	return False

def checkNumericValue(D, field, mini, maxi, debugField=False):
	if not field in D:
		return False
	value = int(D[field])
	if mini<=value<=maxi:
		if debugField:
			print("%s passed: %s (%d/%d)" % (field, D[field], mini, maxi))
		return True
	if debugField or validTestDataSet:
		print("%s failed: %s (%d/%d)" % (field, D[field], mini, maxi))
	return False

def checkPassport(D):
	# byr (Birth Year) - four digits; at least 1920 and at most 2002.
	if not checkNumericValue(D, 'byr', 1920, 2002): return 0

	# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
	if not checkNumericValue(D, 'iyr', 2010, 2020): return 0

	# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
	if not checkNumericValue(D, 'eyr', 2020, 2030): return 0

	# hgt (Height) - a number followed by either cm or in:
	try:
		if D['hgt'].endswith('cm'):
			# If cm, the number must be at least 150 and at most 193.
			cm = int(D['hgt'][:-2])
			if not (150 <= cm <= 193): return 0
		elif D['hgt'].endswith('in'):
			# If in, the number must be at least 59 and at most 76.
			inches = int(D['hgt'][:-2])
			if not (59 <= inches <= 76): return 0
		else: return 0
	except:
		return 0

	# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
	if not valValueEx(D, '#[0-9a-f]{6}', 'hcl'): return 0

	# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
	if not valValueEx(D, '^(amb|blu|brn|gry|grn|hzl|oth)$', 'ecl'): return 0

	# pid (Passport ID) - a nine-digit number, including leading zeroes.
	if not valValueEx(D, '^[0-9]{9}$', 'pid'): return 0

	# cid (Country ID) - ignored, missing or not
	if invalidTestDataSet:
		print(D)
	return 1

def solve(filename, validSet = False, invalidSet = False):
	global validTestDataSet, invalidTestDataSet
	validTestDataSet = validSet; invalidTestDataSet = invalidSet

	fd = open(filename, 'r');

	valids=0
	invalids=0
	D={}
	for line in fd:
		line = line.strip()
		if (line == ""):
			if checkPassport(D): valids+=1
			else: invalids+=1
			D={}
		else:
			for kv in line.split(" "):
				k, v = kv.split(':')
				D[k] = v
	if checkPassport(D): valids+=1
	else: invalids+=1
	print("valids: %d\tinvalids: %d" % (valids, invalids))

solve('input/4.input.valids',   validSet = True)
solve('input/4.input.invalids', invalidSet = True)
solve('input/4.input')
