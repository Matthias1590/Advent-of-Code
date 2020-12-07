with open("Day 6/input.txt", "r") as inputFile:
    puzzleInput = inputFile.read(); outputs = []
for group in puzzleInput.split("\n\n"):
    charList = []
    for char in group.replace("\n", ""):
        if char not in charList:
            charList.append(char)
    outputs.append(len(charList))
print(sum(outputs))