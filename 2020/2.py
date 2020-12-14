# cLx 2020 day 2

def validateWithAlgo1(fd):
	pass_ok = 0; pass_nok = 0
	for line in fd:
		data = line.split()
		mini, maxi = [int(v) for v in data[0].split("-")]
		letter = data[1][0]
		password = data[2]

		cnt = 0
		for c in password:
			if c == letter:
				cnt+=1

		if mini <= cnt <= maxi: pass_ok += 1
		else:                   pass_nok += 1

	print("Algo 1: Ok:", pass_ok, "Nok:", pass_nok)

def validateWithAlgo2(fd):
	pass_ok = 0; pass_nok = 0
	for line in fd:
		data = line.split()
		pos1, pos2 = [int(v) for v in data[0].split("-")]
		letter = data[1][0]
		password = data[2]

		cnt = 0
		if password[pos1-1] == letter:
			cnt+=1
		if password[pos2-1] == letter:
			cnt+=1

		if cnt==1: pass_ok += 1
		else:      pass_nok += 1

	print("Algo 2: Ok:", pass_ok, "Nok:", pass_nok)

with open('input/2.input', 'r') as fd:
	validateWithAlgo1(fd)
	fd.seek(0)
	validateWithAlgo2(fd)
