with open("Day 1/input.txt", "r") as inputFile:
    puzzleInput = inputFile.readlines()
for i in range(len(puzzleInput)):
    for j in range(i, len(puzzleInput)):
        if int(puzzleInput[i].strip()) + int(puzzleInput[j].strip()) == 2020:
            print(int(puzzleInput[i].strip()) * int(puzzleInput[j].strip()))