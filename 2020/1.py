# cLx 2020 day 1

import time
expenses = set(int(v) for v in open('input/1.input', 'r'))

def findSum2020ForTwo():
	for i in expenses:
		j = 2020 - i
		if j in expenses:
			return((i, j), i * j)

def findSum2020ForThree():
	for a, i in enumerate(expenses):
		for j in list(expenses)[a+1:]:
			k = 2020 - i - j
			if k in expenses:
				return((i, j, k), i * j * k)

for f in (findSum2020ForTwo, findSum2020ForThree):
	start = time.time(); numbers, product = f(); end = time.time()
	print(' x '.join([str(i) for i in numbers]), '=', product,"(%.2fms)" % ((end-start)*1000))
