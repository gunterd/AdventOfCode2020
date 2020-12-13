def part1():
    with open('day6input.txt') as f:
        lines = [(line.rstrip('\n')) for line in f]

    startIndex = endIndex = 0
    groups = []

    while endIndex < len(lines):
        while endIndex < len(lines) and lines[endIndex].strip() != "":
            endIndex += 1
        groups.append(lines[startIndex:endIndex])

        startIndex = endIndex + 1
        endIndex = endIndex + 1

    totalCount = 0
    for g in groups:
        answers = set([])
        for person in g:
            for letter in person:
                answers.add(letter)
        totalCount += len(answers)

    print(totalCount) ## 6457

part1()

def part2():
    with open('day6input.txt') as f:
        lines = [(line.rstrip('\n')) for line in f]

    startIndex = endIndex = 0
    groups = []

    while endIndex < len(lines):
        while endIndex < len(lines) and lines[endIndex].strip() != "":
            endIndex += 1
        groups.append(lines[startIndex:endIndex])

        startIndex = endIndex + 1
        endIndex = endIndex + 1

    totalCount = 0
    for g in groups:
        answers = {}
        for person in g:
            for letter in person:
                if letter in answers.keys():
                    answers[letter] += 1
                else:
                    answers[letter] = 1
        
        for a in answers:
            if answers[a] == len(g):
                totalCount += 1
        
        

    print(totalCount) 

part2()