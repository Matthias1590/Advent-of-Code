with open("input.txt", "r") as inputFile:
    puzzleInput = inputFile.readlines(); puzzleInput2 = []
for i in range(len(puzzleInput)):
    puzzleInput2.append("")

curIndex = 0
for line in puzzleInput:
    puzzleInput2[curIndex] += line
    if line == "\n":
        curIndex += 1

totalCount = 0
for passport in puzzleInput2:
    isValid = True
    for keyword in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]:
        if keyword not in passport:
            isValid = False
    if isValid:
        totalCount += 1
print(totalCount)