# number must be the sum of 2 digits from the preamble
def checkNumber(preamble, number):
    for i in range(len(preamble)):
        for j in range(i+1, len(preamble)):
            if preamble[i] + preamble[j] == number:
                return True

    return False

def part1(preambleSize):
    with open('day9input.txt') as f:
    # with open('day9simpleinput.txt') as f:
        lines = [int((line.rstrip('\n'))) for line in f]

        for i in range(preambleSize, len(lines)):
            preamble = lines[i-preambleSize: i]
            if not checkNumber(preamble, lines[i]):
                return lines[i]


print(part1(25))

def sumOfSmallestAndLargest(numRange):
    smallest = numRange[0]
    largest = numRange[0]
    for n in numRange:
        if n < smallest:
            smallest = n
        elif n > largest:
            largest = n
    
    return smallest + largest

def checkNumberPart2(numList, number):
    for i in range(len(numList)):
        for j in range(i+1, len(numList)):
            sumNumber = sum(numList[i:j])
            if sumNumber == number:
                # print('i: ' + str(i) + ' j: ' + str(j))
                return sumOfSmallestAndLargest(numList[i:j])
            if sumNumber > number:
                break

def part2(number):
    with open('day9input.txt') as f:
    # with open('day9simpleinput.txt') as f:
        lines = [int((line.rstrip('\n'))) for line in f]

    print(checkNumberPart2(lines, number))

part2(part1(25))