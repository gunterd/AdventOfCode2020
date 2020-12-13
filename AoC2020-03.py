def part1():
    with open('day3input.txt') as f:
        lines = [(line.rstrip('\n')) for line in f]

    height = 0
    pos = 0
    treeCount = 0
    while height < len(lines):
        if (lines[height][pos] == '#'):
            treeCount += 1
        height += 1
        pos = (pos + 3) % len(lines[0])

    print(treeCount)

part1()

def checkSlope(map, right, down):
    height = 0
    pos = 0
    treeCount = 0

    while height < len(map):
        if(map[height][pos] == '#'):
            treeCount += 1
        height += down
        pos = (pos + right) % len(map[0])

    return treeCount

def part2():
    with open('day3input.txt') as f:
        lines = [(line.rstrip('\n')) for line in f]

    first = checkSlope(lines, 1, 1)
    second = checkSlope(lines, 3, 1)
    third = checkSlope(lines, 5, 1)
    fourth = checkSlope(lines, 7, 1)
    fifth = checkSlope(lines, 1, 2)

    print(first * second * third * fourth * fifth)

part2()
