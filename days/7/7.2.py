import re

def count_bags(current_bag, bags):
    if bags[current_bag] is None:
        return 0
    i = 0
    for bag, amount in bags[current_bag].items():
        i += int(amount) * count_bags(bag, bags)
        i += int(amount)
    return i

with open(r'days\7\input.txt', 'r') as f:
    bags = {}
    for line in f:
        line = line.strip()
        groups = re.split(r'contain |, ', line)
        groups = [re.sub(r'(\s)bag?s?.', '', i) for i in groups]
        # print(groups)
        outer = groups[0]
        if outer not in bags:
                bags[outer] = {}
        if groups[1].strip() == 'no other':
            bags[outer] = None
            continue
        for i in groups[1:]:
            amount, bag, _ = re.split(r' (\D+)', i)
            bags[outer][bag] = amount
    # for key, value in bags.items():
    #     print(key, value)
    print(count_bags('shiny gold', bags))
