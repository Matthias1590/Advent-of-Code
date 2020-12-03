# PART 1
e = 0
with open("input.txt", "r") as inputFile:
    puzzleInput = inputFile.readlines()
for line in puzzleInput:
    a, b, c, d = line.split("-")[0], line.split("-")[0].split(" ")[0], line.split(" ")[1].split(":")[0], line.split(" ")[2]
    if d.count(c) >= int(a) <= int(b):
        e += 1
print(e)

# PART 2
e = 0
with open("input.txt", "r") as inputFile:
    puzzleInput = inputFile.readlines()
for line in puzzleInput:
    a, b, c, d = line.split("-")[0], line.split("-")[1].split(" ")[0], line.split(" ")[1].split(":")[0], line.split(" ")[2]
    if c == d[int(a)-1] != d[int(b)-1] or c == d[int(b)-1] != d[int(a)-1]:
        e += 1
print(e)