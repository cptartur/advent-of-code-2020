import re

with open(r'days\4\input.txt', 'r') as f:
    t = f.read().split('\n\n')
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    fields = {
        'byr': [4, 1920, 2002],
        'iyr': [4, 2010, 2020],
        'eyr': [4, 2020, 2030],
        'hgt': {
            'cm': [150, 193], 
            'in': [59, 76]
            },
        'hcl': [7, '#'],
        'ecl': ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
        'pid': [9],
        'cid': None,
    }
    good = 0
    for passport in t:
        if not all(i in passport for i in required_fields):
            continue
        passport = passport.split()
        for field in passport:
            code, value = field.split(':')
            if code not in fields:
                break
            if code in ('byr', 'iyr', 'eyr'):
                if len(value) != fields[code][0]:
                    break
                if int(value) < fields[code][1] or \
                    int(value) > fields[code][2]:
                    break
            if code == 'hgt':
                _, value, unit = re.split(r'(\d+)', value)
                if value == '' or unit == '':
                    break
                if int(value) < fields[code][unit][0] or \
                   int(value) > fields[code][unit][1]:
                    break
            if code == 'hcl':
                if len(value) != fields[code][0] or \
                   value[0] != fields[code][1]:
                   break
                if re.search(r'[^a-f0-9]', value[1:]):
                    break
            if code == 'ecl':
                if value not in fields[code]:
                    break
            if code == 'pid':
                if len(value) != fields[code][0]:
                    break
        else:
            good += 1
    print(good)

