def part1():
    with open('day1input.txt') as f:
        lines = [(int)(line.rstrip('\n')) for line in f]

    d = {}

    for l in lines:
        d[l] = 2020-l

    for k in d.keys():
        if d[k] in d.keys():
            print("Key: " + str(k) + ", Value: " + str(d[k]) + ", Product: " + str((d[k] * k)))

part1()

def part2():
    with open('day1input.txt') as f:
        lines = [(int)(line.rstrip('\n')) for line in f]

    for l in lines: 
        for m in lines:
            for n in lines:
                if l == m or l == n or m == n:
                    continue
                if l + m + n == 2020:
                    print(l * m * n)


part2()

    