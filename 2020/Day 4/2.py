with open("input.txt", "r") as inputFile:
    puzzleInput = inputFile.readlines(); passports = []
for i in range(len(puzzleInput)):
    passports.append("")

curIndex = 0
for line in puzzleInput:
    passports[curIndex] += line
    if line == "\n":
        curIndex += 1

def parsePass(passport: str):
    newPassport = ""
    passport = passport.replace(" ", "\n")[:-2]
    for line in passport.splitlines():
        newPassport += "'" + line.replace(":", "':'") + "',\n"
    return eval("{" + newPassport + "}")

newPassports = []
for i in range(len(passports)):
    isValid = True
    for keyword in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]:
        if keyword not in passports[i]:
            isValid = False
    if isValid:
        newPassports.append(parsePass(passports[i]))
passports = newPassports

def isValidPass(p: dict):
    byr, iyr, eyr, hgt, hcl, ecl, pid = p["byr"], p["iyr"], p["eyr"], p["hgt"], p["hcl"], p["ecl"], p["pid"]
    if len(byr) != 4 or int(byr) < 1920 or int(byr) > 2002 or len(iyr) != 4 or int(iyr) < 2010 or int(iyr) > 2020 or len(eyr) != 4 or int(eyr) < 2020 or int(eyr) > 2030:
        return 0
    if hgt[-2:] == "cm":
        if int(hgt[:-2]) < 150 or int(hgt[:-2]) > 193:
            return 0
    elif hgt[-2:] == "in":
        if int(hgt[:-2]) < 59 or int(hgt[:-2]) > 76:
            return 0
    if ecl not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"] or len(pid) != 9 or hcl[0] != "#" or len(hcl) != 7:
        return 0
    for char in hcl[1:]:
        if char not in "0123456789abcdef":
            return 0
    return 1

valid = 0
for passport in passports:
    valid += isValidPass(passport)
print(valid)