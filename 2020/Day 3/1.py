with open("Day 3/input.txt", "r") as inputFile:
    puzzleInput1 = inputFile.readlines(); puzzleInput2 = []
for line in puzzleInput1:
    puzzleInput2.append(line.strip() * 3 * len(puzzleInput1))
puzzleInput = puzzleInput2; yPos = 0; xPos = 0; trees = 0
while yPos < len(puzzleInput):
    if puzzleInput[yPos][xPos] == "#":
        trees += 1
    yPos += 1; xPos += 3
print(trees)