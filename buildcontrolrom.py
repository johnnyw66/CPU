
controlWordSize = 24
ACTIVEHIGH = 1
ACTIVELOW = 0

# Definition of our control control lines and which bit in the control word they
# occupy

clLines = [
    {'key':"Cp", 'bit':23, 'active': ACTIVEHIGH, 'desc':"Enable PC count (inc PC)"},
    {'key':"Ep", 'bit':22, 'active': ACTIVEHIGH, 'desc':"Place PC onto the Bus"},
    {'key':"nLm", 'bit':21, 'active': ACTIVELOW, 'desc':"Load contents of Bus into Memory Address Reg"},
    {'key':"nCE", 'bit':20, 'active': ACTIVELOW, 'desc':"Place current data in RAM onto BUS"},

    {'key':"nLi", 'bit':19, 'active': ACTIVELOW, 'desc':"Load contents of Bus into the Instruction Reg"},
    {'key':"nEi", 'bit':18, 'active': ACTIVELOW, 'desc':"Place contents of the Instruction Reg onto the Bus"},
    {'key':"nLa", 'bit':17, 'active': ACTIVELOW, 'desc':"Load contents of the Bus into the A Reg"},
    {'key':"Ea",  'bit':16, 'active': ACTIVEHIGH, 'desc':"Place contents of the A Reg onto the BUS"},

    {'key':"Su",  'bit':15, 'active': ACTIVEHIGH, 'desc':"set ALU function to Subtract (otherwise it will be 'ADD')"},
    {'key':"Eu",  'bit':14, 'active': ACTIVEHIGH, 'desc':"Enable ALU (output directly to B Reg)"},
    {'key':"nLb", 'bit':13, 'active': ACTIVELOW, 'desc':"Load contents of B reg 'bus' into B Reg"},
    {'key':"nLo", 'bit':12, 'active': ACTIVELOW, 'desc':"Load contents of Bus into Output Reg"},

    {'key':"Lr",  'bit':11, 'active': ACTIVEHIGH, 'desc':"Load to RAM (STA op)"},
    {'key':"Lp",  'bit':10, 'active': ACTIVEHIGH, 'desc':"Load PC (JUMP instructions) used with f1 and f0"},
    {'key':"f1",  'bit':9, 'active': ACTIVEHIGH, 'desc':"JUMP condition function bit 1"},
    {'key':"f0",  'bit':8, 'active': ACTIVEHIGH, 'desc':"JUMP condition Function bit 0 {00 -> Carry, 01 -> Non Zero, 10 -> Parity Odd, 11 --> Always}"},
#
    # Free control lines for use later
    {'key':"U0",  'bit':7, 'active': ACTIVEHIGH,'desc':"Some Decription"},
    {'key':"U1",  'bit':6, 'active': ACTIVEHIGH, 'desc':"Some Decription"},
    {'key':"U2",  'bit':5, 'active': ACTIVEHIGH, 'desc':"Some Decription"},
    {'key':"U3",  'bit':4, 'active': ACTIVEHIGH, 'desc':"Some Decription"},

    {'key':"U4",  'bit':3, 'active': ACTIVEHIGH,'desc':"Some Decription"},
    {'key':"U5",  'bit':2, 'active': ACTIVEHIGH, 'desc':"Some Decription"},
    {'key':"U6",  'bit':1, 'active': ACTIVEHIGH, 'desc':"Some Decription"},
    {'key':"U7",  'bit':0, 'active': ACTIVEHIGH, 'desc':"Some Decription"},

]

fetchControlWords = [{'nLm'},{'nLm'},{'nLm'}]

opcodes = [
    {'name':'NOP','bytecode': 0, 'control':
    [
    ]},

    {'name':'STA','bytecode': 1,
    'control':
    [
        {'Eu'}
    ]}
]
def buildNOP():
    NOPWord = 0
    for cl in clLines:
        NOPWord |= (cl['active']^1)<<cl['bit']
    return NOPWord

def getControlLine(controlLineName):
    for cl in clLines:
        if (cl['key'] == controlLineName):
            return cl
    raise Exception(f"Can not find defn for control line {controlLineName}")


def buildControlWord(controlList):
    controlWord = 0
    for clKey in controlList:
        cl = getControlLine(clKey)
        controlWord |= cl['active']<<cl['bit']
    #print("buildControlWord",controlWord)
    return controlWord

def buildMicrocode():
        #integCheck()
    NOPWord = buildNOP()
    print(f"NOP Word {NOPWord:06x}")
    for op in opcodes:
        print(op)
        op['tsize'] = len(op['control'])
        for tStateIndex,tStateCtrlst in enumerate(op['control']):
            controlWord=buildControlWord(tStateCtrlst)
            print(f"{tStateIndex} {controlWord:06x} {op['name']:10} number of tstates {op['tsize']}")

        #print("Control Word {}", op['name'], op['bytecode'],controlWord)
        # 24 bit

    return


try:
    buildMicrocode()
except Exception as e:
    print(f"oh no - check your control data or see a code doctor! {e}")
