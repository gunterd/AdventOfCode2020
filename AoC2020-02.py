class Password:
    def __init__(self, letter, minCount, maxCount, pw):
        self.letter = letter
        self.minCount = minCount
        self.maxCount = maxCount
        self.pw = pw

    def isValid(self):
        letterCount = 0
        for l in self.pw:
            if l == self.letter:
                letterCount += 1
        
        return letterCount >= self.minCount and letterCount <= self.maxCount
            

def part1():
    with open('day2input.txt') as f:
        lines = [(line.rstrip('\n')) for line in f]

    p = Password('a', 1, 2, 'abcde')
    print(p.pw)
    print(p.isValid())

    validCount = 0

    for line in lines:
        splitLine = line.split(' ')
        splitMinMax = splitLine[0].split('-')
        minCount = (int)(splitMinMax[0])
        maxCount = (int)(splitMinMax[1])
        char = splitLine[1][0]
        pw = splitLine[2]

        password = Password(char, minCount, maxCount, pw)
        if password.isValid():
            validCount += 1

    print(validCount)

part1()


class PasswordPart2:
    def __init__(self, letter, index1, index2, pw):
        self.letter = letter
        self.index1 = index1
        self.index2 = index2
        self.pw = pw

    def isValid(self):
        return ( (self.pw[self.index1 - 1] == self.letter and self.pw[self.index2 - 1] != self.letter) or 
        (self.pw[self.index1 - 1] != self.letter and self.pw[self.index2 -1] == self.letter) )
            

def part2():
    with open('day2input.txt') as f:
        lines = [(line.rstrip('\n')) for line in f]

    validCount = 0

    for line in lines:
        splitLine = line.split(' ')
        splitMinMax = splitLine[0].split('-')
        index1 = (int)(splitMinMax[0])
        index2 = (int)(splitMinMax[1])
        char = splitLine[1][0]
        pw = splitLine[2]

        password = PasswordPart2(char, index1, index2, pw)
        if password.isValid():
            validCount += 1

    print(validCount)

part2()