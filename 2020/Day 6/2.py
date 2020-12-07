with open("Day 6/input.txt", "r") as inputFile:
    puzzleInput = inputFile.read(); outputs = []
for group in puzzleInput.split("\n\n"):
    charList = []; newCharList = []
    for char in group.replace("\n", ""):
        if char not in charList:
            charList.append(char)
    for char in charList:
        addChar = True
        for line in group.splitlines():
            if char not in line:
                addChar = False
        if addChar:
            newCharList.append(char)
    outputs.append(len(newCharList))
print(sum(outputs))