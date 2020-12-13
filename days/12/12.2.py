import re

def translate_turn(waypoint, value):
    x, y = waypoint
    d = ([x, y], [-y, x], [-x, -y], [y, -x])
    value = value // 90 
    if direction == 'L':
        value = -value
    return d[value % 4]

with open(r'days\12\input.txt', 'r') as f:
    t = f.read().split()
    for i, v in enumerate(t):
        _, direction, value = re.split(r'(\D)+', v)
        value = int(value)
        if direction == 'S':
            t[i] = ('N', -value)
        elif direction == 'W':
            t[i] = ('E', -value)
        else:
            t[i] = (direction, value)
    pos = [0, 0]
    waypoint = [1, 10]
    for i in t:
        direction, value = i
        if direction == 'F':
            pos[0] += waypoint[0] * value
            pos[1] += waypoint[1] * value
        elif direction == 'N':
            waypoint[0] += value
        elif direction == 'E':
            waypoint[1] += value
        elif direction in ('L', 'R'):
            waypoint = translate_turn(waypoint, value)
    print(sum(list(map(abs, pos))))