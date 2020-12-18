# part 1
#   the rules of operator precedence have changed. Rather than evaluating multiplication
#   before addition, the operators have the same precedence, and are evaluated left-to-right
#   regardless of the order in which they appear.

def solve1(inp, a="", op="", level=0, verbose=True):
	inp = inp.replace(" ", "")
	if verbose:
		print("  "*level, inp, op, a)

	if inp.isnumeric():
		b = int(inp)
	else:
		p = ""
		bracketCount = 0
		while(inp):
			c = inp[-1]; inp=inp[:-1]
			if bracketCount==0:
				if c == '*' or c == '+':
					b = solve1(inp, int(p), op=c, level=level+1, verbose=verbose)
					break
			if c == ')':
				if bracketCount>0:
					p=c+p
				bracketCount+=1
			elif c == '(':
				bracketCount-=1
				if bracketCount==0:
					b = solve1(p, level=level+1, verbose=verbose)
					p = str(b)
				else:
					p=c+p
			else:
				p=c+p

	if op == '+':
		r = b + a
	elif op == '*':
		r = b * a
	else:
		if verbose and level==0: print()
		return b

	if verbose:
		print("  "*level, b, op, a, "=", r)

	return r

print("Part 1")
assert solve1("1 + 2 * 3 + 4 * 5 + 6") == 71
assert solve1("1 + (2 * 3) + (4 * (5 + 6))") == 51
assert solve1("2 * 3 + (4 * 5)") == 26
assert solve1("5 + (8 * 3 + 9 + 3 * 4 * 3)") == 437
assert solve1("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))") == 12240
assert solve1("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2") == 13632

puzzleInputLines = open("input/18.input").read().split('\n')
sumResults = 0
for line in puzzleInputLines:
	line = line.strip()
	if line == "":
		continue
	r = solve1(line, verbose=False)
	sumResults+=r
	print(line, "=", r)
print("Sum is:", sumResults)
assert sumResults == 50956598240016
print()

# part 2
#    Now, addition and multiplication have different precedence levels, but they're
#    not the ones you're familiar with. Instead, addition is evaluated before multiplication.

print("Part 2")
from functools import reduce
import operator
import re

class Node():
	def __init__(self, inp, op=None, level=0, verbose=True):
		self.inp = inp
		self.nodes = []
		self.operator = None
		self.value = None
		self.level = level
		self.verbose = verbose

		if self.verbose:
			print("  "*level+self.inp)
		self.split()
		if self.verbose and self.nodes:
			print("  "*level+self.inp, '=', self.getValue())
			if level == 0:
				print()

	def split(self):
		# check if we can remove one layer of braces
		if self.inp[0] == '(' and self.inp[-1] == ')':
			bracketCount=1
			for i in range(1, len(self.inp)-1):
				c = self.inp[i]
				if c=='(':
					bracketCount+=1
				elif c==')':
					bracketCount-=1
				elif bracketCount==0:
					break
			if bracketCount:
				self.inp = self.inp[1:-1]

		# check the places where we can split
		bracketCount=0
		mulPosisions = []
		addPosisions = []
		for i in range(len(self.inp)):
			c = self.inp[i]
			if c=='(':
				bracketCount+=1
			elif c==')':
				bracketCount-=1
			elif bracketCount==0:
				if c == '+':
					addPosisions.append(i)
				elif c == '*':
					mulPosisions.append(i)

		# split if we can
		if mulPosisions:
			self.operator = operator.mul
			str1 = self.inp[:mulPosisions[0]]
			str2 = self.inp[mulPosisions[0]+1:]
			self.nodes = [Node(str1, level=self.level+1, verbose=self.verbose), Node(str2, level=self.level+1, verbose=self.verbose)]

		elif addPosisions:
			self.operator = operator.add
			str1 = self.inp[:addPosisions[0]]
			str2 = self.inp[addPosisions[0]+1:]
			self.nodes = [Node(str1, level=self.level+1, verbose=self.verbose), Node(str2, level=self.level+1, verbose=self.verbose)]

		else:
			self.value = int(self.inp)

	def __repr__(self):
		return self.inp

	def getValue(self):
		if self.value != None:
			return self.value
		values = [node.getValue() for node in self.nodes]
		return reduce(self.operator, values)


def solve2(inp, verbose=True):
	inp = inp.replace(" ", "")
	val = Node(inp, verbose=verbose).getValue()
	return val

assert solve2("1 + 2 * 3 + 4 * 5 + 6") == 231
assert solve2("1 + (2 * 3) + (4 * (5 + 6))") == 51
assert solve2("2 * 3 + (4 * 5)") == 46
assert solve2("5 + (8 * 3 + 9 + 3 * 4 * 3)") == 1445
assert solve2("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))") == 669060
assert solve2("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2") == 23340

sumResults = 0
for line in puzzleInputLines:
	line = line.strip()
	if line == "":
		continue
	r = solve2(line, verbose=False)
	sumResults+=r
	print(line, "=", r)
print("Sum is:", sumResults)
assert sumResults == 535809575344339
