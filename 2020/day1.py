with open("input.txt", "r") as inputFile:
    puzzleInput = inputFile.readlines()

# PART 1
for i in range(len(puzzleInput)):
    for j in range(i, len(puzzleInput)):
        if int(puzzleInput[i].strip()) + int(puzzleInput[j].strip()) == 2020:
            print(int(puzzleInput[i].strip()) * int(puzzleInput[j].strip()))

# PART 2
for i in range(len(puzzleInput)):
    for j in range(i, len(puzzleInput)):
        for k in range(j, len(puzzleInput)):
            if int(puzzleInput[i].strip()) + int(puzzleInput[j].strip()) + int(puzzleInput[k].strip()) == 2020:
                print(int(puzzleInput[i].strip()) * int(puzzleInput[j].strip()) * int(puzzleInput[k].strip()))