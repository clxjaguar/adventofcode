# cLx 2021 day 10

def solve(filename):
	closuresMatches =          {'(':')', '[':']', '{':'}',  '<':'>'  }
	closuresErrorsPoints =     {')':3,   ']':57,  '}':1197, '>':25137}
	closuresCompletionPoints = {')':1,   ']':2,   '}':3,    '>':4    }

	result1 = 0
	autoCompleteScores = []
	fd = open(filename, 'r')
	for line in [line.strip() for line in fd]:
		stack = []
		syntaxErrorFlag = False
		for c in line:
			if c == '(' or c == '[' or c == '{' or c == '<':
				stack.append(c)

			elif c == ')' or c == ']' or c == '}' or c == '>':
				a = stack.pop()
				if c != closuresMatches[a]:
					print("%s - Expected %s, but found %s instead." % (line, closuresMatches[a], c))
					result1+=closuresErrorsPoints[c]
					syntaxErrorFlag = True
					break
			else:
				raise ValueError(c)

		if not syntaxErrorFlag:
			autoComplete = ""; autoCompleteScore = 0
			while (stack):
				a = stack.pop()
				autoComplete+=closuresMatches[a]
				autoCompleteScore = autoCompleteScore*5 + closuresCompletionPoints[closuresMatches[a]]
			if autoComplete:
				print("%s - Complete by adding %s" % (line, autoComplete))
				autoCompleteScores.append(autoCompleteScore)

	print()
	print("%s: total syntax error score is %d" % (filename, result1))

	autoCompleteScores.sort()
	result2 = autoCompleteScores[int(len(autoCompleteScores)/2)]
	print("%s: median autocomplete score is %d" % (filename, result2))
	print()
	return result1, result2

assert solve('input/10.input.test') == ( 26397,     288957)
assert solve('input/10.input')      == (374061, 2116639949)
