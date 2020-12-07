with open("Day 7/input.txt", "r") as inputFile:
    puzzleInput = inputFile.readlines()
bagList = ["shiny gold"]; lastLength = -1
while len(set(bagList))-1 != lastLength:
    lastLength = len(set(bagList))-1
    for line in puzzleInput:
        for bag in set(bagList):
            if bag in line.split("contain")[1]:
                bagList.append(" ".join(line.split(" ")[0:2]))
print(lastLength)