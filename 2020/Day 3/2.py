with open("input.txt", "r") as inputFile:
    puzzleInput1 = inputFile.readlines(); puzzleInput2 = []
def solve(down, right):
    for line in puzzleInput1:
        puzzleInput2.append(line.strip() * 3 * len(puzzleInput1))
    puzzleInput = puzzleInput2; yPos = 0; xPos = 0; trees = 0
    print(yPos, len(puzzleInput))
    while yPos < len(puzzleInput):
        if puzzleInput[yPos][xPos] == "#":
            trees += 1
        yPos += down; xPos += right
    return trees
print(solve(3, 1))