import re

def find_bag(current_bag, bags):
    if bags[current_bag] is None:
        return False
    if 'shiny gold' in bags[current_bag]:
        return True
    for bag in bags[current_bag]:
        if find_bag(bag, bags):
            return True
    return False

with open(r'days\7\input.txt', 'r') as f:
    bags = {}
    for line in f:
        line = line.strip()
        groups = re.split(r'contain |, ', line)
        groups = [re.sub(r'(\s)bag?s?.', '', i) for i in groups]
        outer = groups[0]
        if outer not in bags:
                bags[outer] = {}
        if groups[1].strip() == 'no other':
            bags[outer] = None
            continue
        for i in groups[1:]:
            amount, bag, _ = re.split(r' (\D+)', i)
            bags[outer][bag] = amount
    total = 0
    for key in bags:
        if find_bag(key, bags):
            total += 1
    print(total)
