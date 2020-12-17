import re

with open(r'days\16\input.txt', 'r') as f:
    r, my_ticket, t = f.read().split('\n\n')
    rules = {}
    for i in r.split('\n'):
        name, v1, v2 = list(filter(None, re.split(r':\s|\s+or', i)))
        rules[name] = (tuple(map(int, v1.split('-'))), tuple(map(int, v2.split('-'))))
    t = [list(map(int, i.split(','))) for i in t.lstrip('nearby tickets:\n').splitlines()]
    e = 0
    for ticket in t:
        for i in ticket:
            for v in rules.values():
                v1, v2 = v
                a, b = v1
                c, d = v2
                if i in range(a, b + 1) or i in range(c, d + 1):
                    break
            else:
                e += i
    print(e)