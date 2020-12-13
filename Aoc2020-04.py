import re

class Passport:
    pass

def isValidPassport(passport):
    return (
        'byr' in passport and
        'iyr' in passport and
        'eyr' in passport and
        'hgt' in passport and
        'hcl' in passport and
        'ecl' in passport and
        'pid' in passport)

def validHeight(hgt):
    height = re.search('^\d+(in|cm)$', hgt)

    if height:
        digits = int(hgt[:-2])
        if hgt[-2:] == 'cm':
            return digits >= 150 and digits <= 193
        if hgt[-2:] == 'in':
            return digits >= 59 and digits <= 76
    return False

def validHairColor(hcl):
    color = re.search('^\#[a-f0-9]{6}$', hcl)
    return color

def validEyeColor(ecl):
    validEyeColors = set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])
    return ecl in validEyeColors

def validPassportId(pid):
    return len(pid) == 9 and int(pid) > 0

def isValidPassportPart2(passport):
    print(passport)
    return (
        ('byr' in passport and len(passport['byr']) == 4 and int(passport['byr']) >= 1920 and int(passport['byr']) <= 2002) and
        ('iyr' in passport and len(passport['iyr']) == 4 and int(passport['iyr']) >= 2010 and int(passport['iyr']) <= 2020) and
        ('eyr' in passport and len(passport['eyr']) == 4 and int(passport['eyr']) >= 2020 and int(passport['eyr']) <= 2030) and
        ('hgt' in passport and validHeight(passport['hgt'])) and
        ('hcl' in passport and validHairColor(passport['hcl'])) and
        ('ecl' in passport and validEyeColor(passport['ecl'])) and
        ('pid' in passport and validPassportId(passport['pid'])))

def part1():
    with open('day4input.txt') as f:
    #with open('day4simpletest.txt') as f:
        lines = [(line.rstrip('\n')) for line in f]

    # Split on totally blank lines (divide into passports)
    # Split on space or \n (divide into fields)
    startIndex = 0
    endIndex = 0
    passports = []
    while endIndex < len(lines):
        while endIndex < len(lines) and lines[endIndex].strip() != "":
            endIndex += 1
        passports.append(lines[startIndex:endIndex])
        startIndex = endIndex + 1
        endIndex = endIndex + 1
    
    # clean up passports
    newPassports = []
    for p in passports:
        newPassport = []
        for l in p:
            newPassport.extend(l.split())
        newPassports.append(newPassport)

    validPassportCount = 0

    for p in newPassports:
        ppObject = {}
        for field in p:
            splitField = field.split(':')
            ppObject[splitField[0]] = splitField[1]

        if isValidPassport(ppObject):
            validPassportCount += 1
    
    print(validPassportCount)



part1()

def part2():
    with open('day4input.txt') as f:
    #with open('day4simpletest.txt') as f:
        lines = [(line.rstrip('\n')) for line in f]

    # Split on totally blank lines (divide into passports)
    # Split on space or \n (divide into fields)
    startIndex = 0
    endIndex = 0
    passports = []
    while endIndex < len(lines):
        while endIndex < len(lines) and lines[endIndex].strip() != "":
            endIndex += 1
        passports.append(lines[startIndex:endIndex])
        startIndex = endIndex + 1
        endIndex = endIndex + 1

    # clean up passports
    newPassports = []
    for p in passports:
        newPassport = []
        for l in p:
            newPassport.extend(l.split())
        newPassports.append(newPassport)

    validPassportCount = 0
    for p in newPassports:
        ppObject = {}
        for field in p:
            splitField = field.split(':')
            ppObject[splitField[0]] = splitField[1]

        if isValidPassportPart2(ppObject):
            validPassportCount += 1

    print(validPassportCount)

part2()
