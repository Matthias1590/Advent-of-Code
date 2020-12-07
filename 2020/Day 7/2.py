with open("Day 7/input.txt", "r") as inputFile:
    puzzleInput = inputFile.readlines()

class Bag:
    def __init__(self, quantity: int, name: str):
        self.quantity = quantity; self.name = name; self.contains = []
        contains = getBags(name)
        if contains:
            for bag in contains:
                self.contains.append(Bag(bag[0], bag[1]))
    def getBagCount(self):
        bagCount = 1
        if self.contains:
            for bag in self.contains:
                bagCount += bag.quantity * bag.getBagCount()
        return bagCount

def getBags(bag):
    bag = " ".join(bag.split(" ")[0:2])
    for line in puzzleInput:
        if bag in " ".join(line.split(" ")[0:2]):
            strBags = line[:-2].split("contain ")[1].split(", "); bags = []
            if "no other bags" in strBags:
                return False
            for strBag in strBags:
                bags.append((int(strBag.split(" ")[0]), " ".join(strBag.split(" ")[1:3])))
            return bags

print(Bag(1, "shiny gold").getBagCount()-1)