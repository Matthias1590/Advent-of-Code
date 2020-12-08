def readInput():
    with open("Day 8/input.txt", "r") as inputFile:
        return inputFile.readlines()
puzzleInput = readInput()

def solve(puzzleInput):
    curIndex = 0; acc = 0
    while curIndex < len(puzzleInput):
        if puzzleInput[curIndex] == "#":
            break
        instruction = puzzleInput[curIndex]; puzzleInput[curIndex] = "#"
        if "acc" in instruction:
            acc += int(instruction.split(" ")[1].replace("+", ""))
        if "jmp" in instruction:
            curIndex += int(instruction.split(" ")[1].replace("+", "")) - 1
        curIndex += 1
    if curIndex == len(puzzleInput):
        print(acc)

jmpList = []; nopList = []
for i in range(len(puzzleInput)):
    instruction = puzzleInput[i]
    if "jmp" in instruction:
        jmpList.append(i)
    if "nop" in instruction:
        nopList.append(i)
for jmp in jmpList:
    puzzleInput = readInput()
    newInput = puzzleInput; newInput[jmp] = newInput[jmp].replace("jmp", "nop")
    solve(newInput)
for nop in nopList:
    puzzleInput = readInput()
    newInput = puzzleInput; newInput[nop] = newInput[nop].replace("nop", "jmp")
    solve(newInput)