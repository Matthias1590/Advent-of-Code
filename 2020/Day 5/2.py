with open("Day 5/input.txt", "r") as inputFile:
    puzzleInput = inputFile.readlines(); seats =[]
for seat in puzzleInput:
    seat = seat.strip(); row = range(128)
    for char in seat[0:7]:
        if char == "F":
            row = row[:int(len(row)/2)]
        elif char == "B":
            row = row[int(len(row)/2):]
    row = row[0]; column = range(8)
    for char in seat[7:]:
        if char == "R":
            column = column[int(len(column)/2):]
        elif char == "L":
            column = column[:int(len(column)/2)]
    column = column[0]; seats.append(row * 8 + column)
curSeat = seats[0]
for curSeat in range(len(seats)):
    if curSeat not in seats and curSeat + 1 in seats and curSeat - 1 in seats:
        print(curSeat)