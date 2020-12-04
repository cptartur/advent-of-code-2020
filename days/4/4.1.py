with open(r'days\4\input.txt', 'r') as f:
    t = f.read().split('\n\n')
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    good = 0
    for line in t:
        if all(i in line for i in required_fields):
            good += 1
    print(good)