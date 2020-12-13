import re

def part1Attempt2(adjLists, source, dest):
    visited = {}
    for bag in adjLists:
        visited[bag] = False
    
    queue = []
    queue.append(source)
    visited[source] = True

    while queue:
        bag = queue.pop(0)
        if bag == dest:
            return True
        
        for n in adjLists[bag]:
            if visited[n[0]] == False:
                queue.append(n[0])
                visited[n[0]] = True
    return False


def part1():
    with open('day7input.txt') as f:
    # with open('day7simpleinput.txt') as f:
        lines = [(line.rstrip('\n')) for line in f]

    adjLists = {}

    for line in lines:
        containers = line.split("contain")
        source = containers[0].strip()[0:-5]
        destinations = containers[1].split(",")
        
        for d in destinations:
            d = d.strip()
            count = re.search(r"^(\d+) (.+)bags*\.*", d)
            if source not in adjLists:
                adjLists[source] = []
            if count:
                adjLists[source].append([count.group(2).strip(), count.group(1)])
    total = 0
    for s in adjLists:
        found = part1Attempt2(adjLists, s, 'shiny gold')
        if found:
            total += 1
    
    print(total - 1) # Bag can't contain itself
        
part1()

def totalBagsInSingleBag(adjLists, bag):
    if len(adjLists[bag]) == 0:
        return 0
    
    totalBags = 0
    for b in adjLists[bag]:
        totalBags += (b[1] + b[1] * totalBagsInSingleBag(adjLists, b[0]))

    return totalBags

def part2():
    with open('day7input.txt') as f:
    # with open('day7simpleinput.txt') as f:
    # with open('day7part2simple.txt') as f:
        lines = [(line.rstrip('\n')) for line in f]

    adjLists = {}

    for line in lines:
        containers = line.split("contain")
        source = containers[0].strip()[0:-5]
        destinations = containers[1].split(",")
        
        for d in destinations:
            d = d.strip()
            count = re.search(r"^(\d+) (.+)bags*\.*", d)
            if source not in adjLists:
                adjLists[source] = []
            if count:
                adjLists[source].append([count.group(2).strip(), int(count.group(1))])
    
    print(totalBagsInSingleBag(adjLists, 'shiny gold'))
    # print(totalBagsInSingleBag(adjLists, 'dark red'))
    # print(totalBagsInSingleBag(adjLists, 'dark orange'))
    # print(totalBagsInSingleBag(adjLists, 'dark yellow'))
    # print(totalBagsInSingleBag(adjLists, 'dark green'))
    # print(totalBagsInSingleBag(adjLists, 'dark blue'))
    # print(totalBagsInSingleBag(adjLists, 'dark violet'))

part2()