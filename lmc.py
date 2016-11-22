mailboxes = [0]*100
pc = 0
accumulator = 0
compiled = False
labels = {}
def reset():
	global mailboxes, pc, accumulator, compiled
	mailboxes = [0]*100
	pc = 0
	accumulator = 0
	compiled = False



def compile(code):
	"""Function to translate all mnemonics and labels to decimal instructions"""
	global mailboxes, compiled, labels
	lmcInstructions = ['ADD', 'SUB', 'LDA', 'STA', 'INP', 'OUT', 'HLT', 'BRZ', 'BRP', 'BRA']
	code = code.split('\n')
	code = [x for x in code if x != '']
	codeAndLoc = list(enumerate(code))
	
	#Resolve labels
	for locAndInstruction in codeAndLoc:
		instruction = locAndInstruction[1].lstrip().rstrip()
		instructionParts = instruction.split(' ')
		if instructionParts[0] not in lmcInstructions:
			loc = locAndInstruction[0]
			labels[instructionParts[0]] = "{0:0=2d}".format(loc)
			print(instructionParts[0] + ' is a label for address: ' + str(locAndInstruction[0]))
	for locAndInstruction in codeAndLoc:
		instruction = locAndInstruction[1].lstrip().rstrip()
		instructionParts = instruction.split(' ')
		if 'ADD' in instructionParts:
			if instructionParts[0] == 'ADD':
				mailboxes[locAndInstruction[0]] = str(1) + str(labels[instructionParts[1]])
			elif instructionParts[1] == 'ADD':
				try:
					mailboxes[locAndInstruction[0]] = str(1) + str(labels[instructionParts[2]])
				except:
					raise ValueError("Need mailbox address to add but none received")
		elif 'SUB' in instructionParts:
			if instructionParts[0] == 'SUB':
				mailboxes[locAndInstruction[0]] = str(2) + str(labels[instructionParts[1]])
			elif instructionParts[1] == 'SUB':
				try:
					mailboxes[locAndInstruction[0]] = str(2) + str(labels[instructionParts[2]])
				except:
					raise ValueError("Need mailbox address to subtract but none received")
		elif 'STA' in instructionParts:
			if instructionParts[0] == 'STA':
				mailboxes[locAndInstruction[0]] = str(3) + str(labels[instructionParts[1]])
			elif instructionParts[1] == 'STA':
				try:
					mailboxes[locAndInstruction[0]] = str(3) + str(labels[instructionParts[2]])
				except:
					raise ValueError("Need mailbox address to store to but none received")
		elif 'LDA' in instructionParts:
			if instructionParts[0] == 'LDA':
				mailboxes[locAndInstruction[0]] = str(5) + str(labels[instructionParts[1]])
			elif instructionParts[1] == 'LDA':
				try:
					mailboxes[locAndInstruction[0]] = str(5) + str(labels[instructionParts[2]])
				except:
					raise ValueError("Need mailbox address to load from but none received")
		elif 'BRA' in instructionParts:
			if instructionParts[0] == 'BRA':
				mailboxes[locAndInstruction[0]] = str(6) + str(labels[instructionParts[1]])
			elif instructionParts[1] == 'BRA':
				try:
					mailboxes[locAndInstruction[0]] = str(6) + str(labels[instructionParts[2]])
				except:
					raise ValueError("Need mailbox address to jump/branch to but none received")
		elif 'BRZ' in instructionParts:
			if instructionParts[0] == 'BRZ':
				mailboxes[locAndInstruction[0]] = str(7) + str(labels[instructionParts[1]])
			elif instructionParts[1] == 'BRZ':
				try:
					mailboxes[locAndInstruction[0]] = str(7) + str(labels[instructionParts[2]])
				except:
					raise ValueError("Need mailbox address to jump/branch to but none received")
		elif 'BRP' in instructionParts:
			if instructionParts[0] == 'BRP':
				mailboxes[locAndInstruction[0]] = str(8) + str(labels[instructionParts[1]])
			elif instructionParts[1] == 'BRP':
				try:
					mailboxes[locAndInstruction[0]] = str(8) + str(labels[instructionParts[2]])
				except:
					raise ValueError("Need mailbox address to jump/branch to but none received")
		elif 'INP' in instructionParts:
			mailboxes[locAndInstruction[0]] = str(901)
		elif 'OUT' in instructionParts:
			mailboxes[locAndInstruction[0]] = str(902)
		elif 'DAT' in instructionParts:
			if instructionParts[0] == 'DAT':
				try:
					mailboxes[locAndInstruction[0]] = str(instructionParts[1])
				except:
					raise ValueError("Need a value to store")
			elif instructionParts[1] == 'DAT' and len(instructionParts) > 2:
				mailboxes[locAndInstruction[0]] = str(instructionParts[2])
	print(mailboxes)
	compiled = True
def run():
	global pc, accumulator, mailboxes, labels
	pc = 0
	nextInstruction = mailboxes[pc]
	while nextInstruction != 0:
		#print('Executing', nextInstruction, '...')
		if nextInstruction[0] == '1':
			accumulator += int(mailboxes[int(nextInstruction[1:3])])
			#print('Accumulator is now', accumulator)
		elif nextInstruction[0] == '2':
			accumulator -= int(mailboxes[int(nextInstruction[1:3])])
			#print('Accumulator is now', accumulator)
		elif nextInstruction[0] == '3':
			mailboxes[int(nextInstruction[1:3])] = accumulator
			#print('Mailbox ' + str(nextInstruction[1:3]) + ' set to ' + str(accumulator))
		elif nextInstruction[0] == '5':
			accumulator = int(mailboxes[int(nextInstruction[1:3])])
			#print('Accumulator set to', accumulator)
		elif nextInstruction[0] == '6':
			pc = int(nextInstruction[1:3])-1
		elif nextInstruction[0] == '7':
			if accumulator == 0:
				pc = int(nextInstruction[1:3])-1
		elif nextInstruction[0] == '8':
			if accumulator >= 0:
				pc = int(nextInstruction[1:3])-1
		elif nextInstruction == '901':
			inbox = int(input("Enter a number as input. Must be between -999 and 999\n"))
			accumulator = inbox
		elif nextInstruction == '902':
			print(str(accumulator))
		pc += 1
		nextInstruction = mailboxes[pc]


		
def lmc():
	global compiled
	print("Input your code. One instruction on each line\nEnter 'r' to reset\nEnter ';' to compile\nEnter '>' to run after the program has been compiled\nEnter 'q' to quit")
	newCode = input(">>>")
	code = ""
	while newCode != "q":
		if newCode == 'r':
			code = ""
			reset()
		elif newCode == ';':
			compile(code)
		elif newCode == '>':
			if compiled:
				run()
			else:
				print("Program not compiled. Please type ';' to compile")
		else:
			code = code+'\n'+newCode
		newCode = input(">>>")
		
lmc()
