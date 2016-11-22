boxes = [1] * 100
pc = 0
accumulator = 0

def load(boxId):
    global accumulator
    accumulator = boxes[boxid]
def store(boxId):
    boxes[boxId] = accumulator
def add(boxId):
    global accumulator
    print(boxId)
    print(boxes[boxId])
    accumulator += boxes[boxId]
def sub(boxId):
    global accumulator
    accumulator -= boxes[boxId]
def inp():
    global accumulator
    a = input("Input a number between -999 and 999\n")
    if -999 <= int(a) <= 999:
        try:
            accumulator = int(a)
        except e:
            print(e)
def out():
    print(str(accumulator))
def brz(boxId):
    if accumulator == 000:
        pc = boxId
def brp(boxId):
    if accumulator >= 000:
        pc = boxId
def bra(boxId):
    pc = boxId
def dat(loc, data):
    boxes[loc] = data
def evaluate(code):
    global pc
    pc = 0
    while pc < len(code):
        instruction = code[pc].strip(' ')
        if instruction[:3] == 'LDA':
            boxId = instruction[len(instruction)-1-instruction.index('A'):len(instruction)]
            try:
                boxId = int(boxId)
            except:
                for a in code:
                    if a[:len(a)-len(boxId)].strip(' ') == boxId:
                        boxId = code.index(a)
            load(boxId)
        if instruction[:3] == "STA":
            boxId = instruction[len(instruction)-1-instruction.index('A'):len(instruction)]
            try:
                boxId = int(boxId)
            except:
                for a in code:
                    if a[:len(a)-len(boxId)].strip(' ') == boxId:
                        boxId = code.index(a)
            store(boxId)
        if instruction[:3] == "ADD":
            boxId = instruction[4:]
            try:
                boxId = int(boxId)
                #print("BOXID 2 ", boxId)
            except:
                for a in code:
                    print(a[:len(a)-1-len(boxId)].strip(' '))
                    if a[:len(a)-1-len(boxId)].strip(' ') == boxId:
                        boxId = code.index(a)
                        #print("BOXID 3 ", boxId)
            add(boxId)
        if instruction[:3] == "SUB":
            boxId = instruction[len(instruction)-1-instruction.index('B'):len(instruction)]
            try:
                boxId = int(boxId)
            except:
                for a in code:
                    if a[:len(a)-len(boxId)].strip(' ') == boxId:
                        boxId = code.index(a)
            sub(boxId)
        if instruction[:3] == "INP":
            inp()
        if instruction[:3] == "OUT":
            out()
        pc += 1
instructions = {"LDA": load, "STA" : store, "ADD" : add, "SUB" : sub, "INP" : inp, "OUT" : out, "BRZ" : brz, "BRP" : brp, "BRA" : bra, "DAT" : dat}

def interactive():
    while True:
        line = input("Enter lmc code. Separate each instruction with a comma\n")
        code = line.split(',')
        evaluate(code)
interactive()
    

