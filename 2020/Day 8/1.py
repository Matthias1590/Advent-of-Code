with open("Day 8/input.txt", "r") as inputFile:
    puzzleInput = inputFile.readlines()
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
print(acc)