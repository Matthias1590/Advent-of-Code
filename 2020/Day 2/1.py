with open("Day 2/input.txt", "r") as inputFile:
    puzzleInput = inputFile.readlines()
e = 0
for line in puzzleInput:
    a, b, c, d = line.split("-")[0], line.split("-")[0].split(" ")[0], line.split(" ")[1].split(":")[0], line.split(" ")[2]
    if d.count(c) >= int(a) <= int(b):
        e += 1
print(e)