def countDifferences(arr):
    oneDifferences = 0
    twoDifferences = 0
    threeDifferences = 0
    for i in range(1, len(arr)):
        if arr[i] - arr[i-1] == 1:
            oneDifferences += 1
        elif arr[i] - arr[i-1] == 2:
            twoDifferences += 1
        elif arr[i] - arr[i-1] == 3:
            threeDifferences += 1

    return oneDifferences * threeDifferences


def part1(inputFile):
    with open(inputFile) as f:
        lines = [int((line.rstrip('\n'))) for line in f]

    lines.append(0) #append outlet
    lines.sort()
    lines.append(lines[len(lines)-1] + 3) # append built in adapter
    print(countDifferences(lines))

part1('day10simpleinput.txt')
part1('day10simpleinput2.txt')
part1('day10input.txt')

def pathsToEnd(adapters, startIndex, cache):
    if startIndex in cache:
        return cache[startIndex]

    if startIndex == len(adapters) - 1: # we're at the end
        cache[startIndex] = 1
        return 1

    jolts = adapters[startIndex]

    totalPaths = 0
    if jolts+1 in adapters:
        totalPaths += pathsToEnd(adapters, adapters.index(jolts+1), cache)
    if jolts+2 in adapters:
        totalPaths += pathsToEnd(adapters, adapters.index(jolts+2), cache)
    if jolts+3 in adapters:
        totalPaths += pathsToEnd(adapters, adapters.index(jolts+3), cache)

    cache[startIndex] = totalPaths
    return totalPaths

def part2(inputFile):
    with open(inputFile) as f:
        lines = [int((line.rstrip('\n'))) for line in f]

    lines.append(0) #append outlet
    lines.sort()
    lines.append(lines[len(lines)-1] + 3) # append built in adapter

    print(pathsToEnd(lines, 0, {}))

part2('day10simpleinput.txt')
part2('day10simpleinput2.txt')
part2('day10input.txt')
