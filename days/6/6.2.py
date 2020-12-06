import functools

with open(r'days\6\input.txt', 'r') as f:
    t = f.read().split('\n\n')
    t = [i.splitlines() for i in t]
    total = 0
    for group in t:
        sets = []
        for s in group:
            sets.append(set(s))
        total += len(functools.reduce(lambda x, y: x.intersection(y), sets))
    print(total)