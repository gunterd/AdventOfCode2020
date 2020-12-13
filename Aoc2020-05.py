def convertRowToInt(row):
    row = row.replace("F", "0")
    row = row.replace("B", "1")
    return int(row, 2)

def convertColToInt(col):
    col = col.replace("L", "0")
    col = col.replace("R", "1")
    return int(col, 2)

def convertSeatToId(line):
    row = convertRowToInt(line[:7])
    col = convertColToInt(line[-3:])
    id = row * 8 + col
    return id

def part1():
    with open('day5input.txt') as f:
        lines = [(line.rstrip('\n')) for line in f]

    maxId = 0
    for l in lines:
        seatId = convertSeatToId(l)
        if seatId > maxId:
            maxId = seatId
    return maxId

def part2():
    with open('day5input.txt') as f:
        lines = [(line.rstrip('\n')) for line in f]

    maxId = 922 # From part 1
    seats = [False for x in range(maxId+1)]

    for l in lines:
        seatId = convertSeatToId(l)
        seats[seatId] = True

    for index, seat in enumerate(seats):
        if index == 0 or index == (len(seats) - 1):
            continue
        if not seat and seats[index-1] and seats[index+1]:
            return index


def testConvertRowToInt():
    assert convertRowToInt("F") == 0
    assert convertRowToInt("B") == 1
    assert convertRowToInt("BF") == 2
    assert convertRowToInt("FBFBBFF") == 44

def testConvertColToInt():
    assert convertColToInt("L") == 0
    assert convertColToInt("R") == 1
    assert convertColToInt("RL") == 2
    assert convertColToInt("RLR") == 5

def testConvertSeatToId():
    assert convertSeatToId("BFFFBBFRRR") == 567
    assert convertSeatToId("FFFBBBFRRR") == 119
    assert convertSeatToId("BBFFBBFRLL") == 820

testConvertRowToInt()
testConvertColToInt()
testConvertSeatToId()

print(part1())
print(part2())