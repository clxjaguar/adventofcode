# cLx 2022 day 2

def solve1(filename):
	fd = open(filename, 'r')

	totalScore = 0

	for line in fd:
		opponentChoice, yourChoice = line.strip().split()

		#    A for Rock,           X for Rock,
		#    B for Paper,          Y for Paper,
		#    C for Scissors        Z for Scissors

		if   opponentChoice == "A" and yourChoice == "X": r= 0
		elif opponentChoice == "A" and yourChoice == "Y": r= 1
		elif opponentChoice == "A" and yourChoice == "Z": r=-1
		elif opponentChoice == "B" and yourChoice == "X": r=-1
		elif opponentChoice == "B" and yourChoice == "Y": r= 0
		elif opponentChoice == "B" and yourChoice == "Z": r= 1
		elif opponentChoice == "C" and yourChoice == "X": r= 1
		elif opponentChoice == "C" and yourChoice == "Y": r=-1
		elif opponentChoice == "C" and yourChoice == "Z": r= 0
		else: assert()

		if   r ==-1: score = 0
		elif r == 0: score = 3
		elif r == 1: score = 6
		else: assert()

		if   yourChoice == "X": score+= 1
		elif yourChoice == "Y": score+= 2
		elif yourChoice == "Z": score+= 3
		else: assert()

		# ~ print(yourChoice, opponentChoice, score)
		totalScore+= score

	print(totalScore)
	return totalScore

def solve2(filename):
	fd = open(filename, 'r')

	totalScore = 0

	for line in fd:
		opponentChoice, roundResult = line.strip().split()

		#    A for Rock,       X means you need to lose,
		#    B for Paper,      Y means you need to end the round in a draw,
		#    C for Scissors    and Z means you need to win

		if roundResult == "Y": yourChoice = opponentChoice
		elif opponentChoice == "A" and roundResult == "X": yourChoice = "C"
		elif opponentChoice == "A" and roundResult == "Z": yourChoice = "B"
		elif opponentChoice == "B" and roundResult == "X": yourChoice = "A"
		elif opponentChoice == "B" and roundResult == "Z": yourChoice = "C"
		elif opponentChoice == "C" and roundResult == "X": yourChoice = "B"
		elif opponentChoice == "C" and roundResult == "Z": yourChoice = "A"
		else: assert()

		if   roundResult == "X": score = 0
		elif roundResult == "Y": score = 3
		elif roundResult == "Z": score = 6
		else: assert()

		if   yourChoice == "A": score+= 1
		elif yourChoice == "B": score+= 2
		elif yourChoice == "C": score+= 3
		else: assert()

		# ~ print(opponentChoice, yourChoice, roundResult, score)
		totalScore+= score

	print(totalScore)
	return totalScore

assert solve1('input/2.input.test') == 15
assert solve1('input/2.input') == 10816

assert solve2('input/2.input.test') == 12
assert solve2('input/2.input') == 11657
