# cLx 2020 day 8

import time

def start():
	global startTime
	startTime = time.time()

def stop():
	global startTime
	return (time.time() - startTime) * 1000

def run(code, debugLevel=0):
	PC = 0; A = 0
	ran = set()
	while True:
		OP = code[PC][0]
		if debugLevel >= 2:
			print(" %5d %s %s" % (PC, OP, code[PC][1]))
		if PC in ran:
			if debugLevel >= 1:
				print("*** BREAKPOINT: PC=%d A=%d ***" % (PC, A))
			return False
		ran.add(PC)

		if   OP == 'acc': A+=int(code[PC][1]); PC+=1
		elif OP == 'jmp': PC+=int(code[PC][1])
		elif OP == 'nop': PC+=1

		else:
			print("*** ERROR: Unknow Instruction: %s PC=%D ***" % (op, PC))
			exit()

		if PC == len(code):
			print("*** END OF PROGRAM: PC=%d A=%d ***" % (PC, A))
			return True

def indent(level):
	return " "*level*2

def reverseRun(i, code, traversed, jumpsFrom, nopsFrom, level=0, patched=False, patchLine=None, patchLinesOK=set(), verbose=False):
	while(True):
		if i in traversed:
			if verbose: print(indent(level)+str(i)+("P" if patched else ""), " ".join(code[i]), "[CYCLE DETECTED]")
			return
		elif i < 0:
			if verbose: print(indent(level)+str(i)+("P" if patched else ""), " ".join(code[i]), "[INVALID ADDRESS]")
			return
		elif i == 0:
			if verbose: print(indent(level)+str(i)+("P" if patched else ""), " ".join(code[i]), "[ENTRY POINT FOUND]")
			patchLinesOK.add(patchLine)
			# ~ run(code, debugLevel=1) # possible to run automatically from here
			return True
		elif i < len(code):
			if verbose: print(indent(level)+str(i)+("P" if patched else ""), " ".join(code[i]))
		else:
			if verbose: print(indent(level)+str(i)+("P" if patched else ""), "[END OF PROGRAM]")

		traversed.add(i)

		if i in jumpsFrom:
			for addresse in jumpsFrom[i]:
				r = reverseRun(addresse, code, traversed.copy(), jumpsFrom, nopsFrom, level+1, patched, patchLine, patchLinesOK, verbose=verbose)
				if (r): return patchLinesOK

		if i in nopsFrom and not patched:
			for addresse in nopsFrom[i]:
				bkp = code[addresse].copy()
				code[addresse][0] = "jmp"
				r = reverseRun(addresse, code, traversed.copy(), jumpsFrom, nopsFrom, level+1, patched=True, patchLine=addresse, patchLinesOK=patchLinesOK, verbose=verbose)
				if (r): return patchLinesOK
				code[addresse] = bkp

		if code[i-1][0] == "jmp" and not patched:
			patchLine=i-1;
			bkp = code[patchLine].copy()
			code[patchLine][0] = "nop"
			r = reverseRun(patchLine, code, traversed.copy(), jumpsFrom, nopsFrom, level+1, patched=True, patchLine=patchLine, patchLinesOK=patchLinesOK, verbose=verbose)
			if (r): return patchLinesOK
			code[patchLine] = bkp

		if code[i-1][0] != "jmp":
			i-=1
		else:
			break # heck, no!

	return patchLinesOK

def solve(filename):
	f = open(filename, 'r')
	code = []
	for line in f:
		code.append((line.strip().split()))

	# part 1
	run(code, debugLevel=1)

	# part 2
	start()
	for i in range(len(code)):
		bkp = code[i].copy()
		if code[i][0] == 'jmp':    code[i][0] = 'nop'
		elif code[i][0] == 'nop':  code[i][0] = 'jmp'
		else:                      continue

		if run(code):
			print(i, bkp, '=>', code[i])
			print("Finished bruteforce method with success in %fms" % stop())
			break
		else:
			code[i] = bkp

	# now, part 2 in nightmare mode! somebody asked for this!
	code[i] = bkp # restore bad code first

	jumpsFrom = {}
	nopsFrom = {}
	for i, instr in enumerate(code):
		op = instr[0]; arg = int(instr[1])
		if op == "jmp":
			if i+arg not in jumpsFrom:
				jumpsFrom[i+arg] = []
			jumpsFrom[i+arg].append(i)
		elif op == "nop":
			if i+arg not in nopsFrom:
				nopsFrom[i+arg] = []
			nopsFrom[i+arg].append(i)

	print("\nReverse jumps table:", jumpsFrom, "\n")
	print("Reverse nops table: ", nopsFrom, "\n")

	i = len(code)
	traversed = set()
	start()
	patchLine = reverseRun(i, code, traversed, jumpsFrom, nopsFrom)
	print("Finished reversed recursive search with success in %fms" % stop())

	# again! again! print the tree, we don't care abount benchmarking!
	traversed = set()
	if len(patchLine):
		code[patchLine.pop()] = bkp # restore bad code once more time
	patchLine = reverseRun(i, code, traversed, jumpsFrom, nopsFrom, verbose=True)

	if len(patchLine):
		print("linePatched:", patchLine, "\n")
	run(code)

solve("input/8.input")

