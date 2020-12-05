with open("Day 2/input.txt", "r") as inputFile:
    puzzleInput = inputFile.readlines()
e = 0
for line in puzzleInput:
    a, b, c, d = line.split("-")[0], line.split("-")[1].split(" ")[0], line.split(" ")[1].split(":")[0], line.split(" ")[2]
    if c == d[int(a)-1] != d[int(b)-1] or c == d[int(b)-1] != d[int(a)-1]:
        e += 1
print(e)