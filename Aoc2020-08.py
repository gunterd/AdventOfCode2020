
def parseInstruction(ins, acc, p):
    splitInstruction = ins.split()
    action = splitInstruction[0]
    value = int(splitInstruction[1])

    if action == 'nop':
        p += 1
    elif action == 'jmp':
        p += value
    elif action == 'acc':
        p += 1
        acc += value

    return acc, p

def part1():
    with open('day8input.txt') as f:
    # with open('day8simpleinput.txt') as f:
        lines = [(line.rstrip('\n')) for line in f]

    accumulator = 0
    pointer = 0
    visited = [False for l in lines]

    while pointer < len(lines):
        if visited[pointer]:
            break
        visited[pointer] = True

        accumulator, pointer = parseInstruction(lines[pointer], accumulator, pointer)

    print(accumulator)


part1()

def part2():
    with open('day8input.txt') as f:
    # with open('day8simpleinput.txt') as f:
        lines = [(line.rstrip('\n')) for line in f]
    
    for i in range(len(lines)):

        accumulator = 0
        pointer = 0
        visited = [False for l in lines]

        ended = True

        originalInstruction = lines[i]
        if lines[i][0:3] == 'nop':
            lines[i] = lines[i].replace('nop', 'jmp')
        elif lines[i][0:3] == 'jmp':
            lines[i] = lines[i].replace('jmp', 'nop')

        while pointer < len(lines):
            if visited[pointer]:
                ended = False
                break

            visited[pointer] = True

            accumulator, pointer = parseInstruction(lines[pointer], accumulator, pointer)

        if ended:
            print(accumulator)
            break

        lines[i] = originalInstruction

part2()