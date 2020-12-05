with open("Day 3/input.txt", "r") as inputFile:
    puzzleInput1 = inputFile.readlines(); puzzleInput2 = []
def solve(right, down):
    for line in puzzleInput1:
        puzzleInput2.append(line.strip() * right * len(puzzleInput1))
    puzzleInput = puzzleInput2; yPos = 0; xPos = 0; trees = 0
    while yPos < len(puzzleInput):
        if puzzleInput[yPos][xPos] == "#":
            trees += 1
        yPos += down; xPos += right
    return trees
print(solve(1, 1) * solve(5, 1) * solve(7, 1) * solve(1, 2) * solve(3, 1))