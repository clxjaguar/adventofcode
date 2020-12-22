# cLx 2020 day 22

def runGame(deckPlayer1, deckPlayer2, game=1, part2Rules=False):
	wonAtGame = 0
	if part2Rules:
		print("=== Game %d ===" % game)
		previousDecksConfs=set()

	round=0
	while len(deckPlayer1) != 0 and len(deckPlayer2):
		round+=1
		print()
		if part2Rules:
			print("-- Round %d (Game %d) --" % (round, game))
		else:
			print("-- Round %d --" % round)
		print("Player 1's deck:", ", ".join(map(str, deckPlayer1)))
		print("Player 2's deck:", ", ".join(map(str, deckPlayer2)))

		# Before either player deals a card, if there was a previous round in this game that had exactly the same cards in the same order in the same players' decks, the game instantly ends in a win for player 1. Previous rounds from other games are not considered. (This prevents infinite games of Recursive Combat, which everyone agrees is a bad idea.)

		if part2Rules:
			decksConf = (tuple(deckPlayer1), tuple(deckPlayer2))
			if decksConf in previousDecksConfs:
				print("PLAYER 1 WINNER BY DEFAULT")
				return 1, game
			previousDecksConfs.add(decksConf)

		# Otherwise, this round's cards must be in a new configuration; the players begin the round by each drawing the top card of their deck as normal.

		cardPlayer1 = deckPlayer1.pop(0)
		cardPlayer2 = deckPlayer2.pop(0)
		print("Player 1 plays:", cardPlayer1)
		print("Player 2 plays:", cardPlayer2)

		# If both players have at least as many cards remaining in their deck as the value of the card they just drew, the winner of the round is determined by playing a new game of Recursive Combat

		assert cardPlayer1 != cardPlayer2
		if part2Rules and len(deckPlayer1) >= cardPlayer1 and len(deckPlayer2) >= cardPlayer2:
			print("Playing a sub-game to determine the winner...\n")
			wonPlayer, wonAtGame = runGame(deckPlayer1[:cardPlayer1], deckPlayer2[:cardPlayer2], game=max(game, wonAtGame)+1, part2Rules=True)
			print("...anyway, back to game %d." % game)
		elif cardPlayer1 > cardPlayer2:
			wonPlayer = 1
		elif cardPlayer2 > cardPlayer1:
			wonPlayer = 2

		if part2Rules:
			print("Player %d wins round %d of game %d!" % (wonPlayer, round, game))
		else:
			print("Player %d wins the round!" % (wonPlayer))

		if wonPlayer == 1:
			deckPlayer1.append(cardPlayer1)
			deckPlayer1.append(cardPlayer2)
		elif wonPlayer == 2:
			deckPlayer2.append(cardPlayer2)
			deckPlayer2.append(cardPlayer1)
		else:
			exit(-1)

	if part2Rules:
		print("The winner of game %d is player %d!" % (game, wonPlayer))
	print()

	return wonPlayer, max(game, wonAtGame)

def calculateScore(deck):
	score = 0
	for value, card in zip(range(len(deck), 0, -1), deck):
		score+= value * card
	return score

def solve(filename, part2Rules=False):
	print("****", filename, "****")
	if part2Rules:
		print("** Recursive Combat Rules **")
		print()

	deckPlayer1, deckPlayer2 = [list(map(int, deck.split(":")[1].split())) for deck in open(filename).read().split("\n\n")]
	winner, maxGames = runGame(deckPlayer1, deckPlayer2, part2Rules=part2Rules)

	print("== Post-game results ==")
	print("Player 1's deck:", ", ".join(map(str, deckPlayer1)))
	print("Player 2's deck:", ", ".join(map(str, deckPlayer2)))

	score = calculateScore((deckPlayer1, deckPlayer2)[winner-1])
	print("SCORE: %d%s" % (score, (" (according to Recursive Combat Rules, with %d games)" % maxGames) if part2Rules else ""))
	print()
	return score

# part 1
assert solve("input/22.input.test") == 306
assert solve("input/22.input") == 35818

# part 2
assert solve("input/22.input.test", part2Rules=True) == 291
assert solve("input/22.input", part2Rules=True) == 34771
