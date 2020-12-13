import re

def translate_turn(prev_direction, direction, value):
    d = ('N', 'E', 'S', 'W')
    value = value // 90 
    if direction == 'L':
        value = -value
    i = d.index(prev_direction)
    return d[(i + value) % 4]

with open(r'days\12\input.txt', 'r') as f:
    t = f.read().split()
    facing = 'E'
    for i, v in enumerate(t):
        _, direction, value = re.split(r'(\D)+', v)
        value = int(value)
        if direction == 'F':
            direction = facing
        if direction == 'S':
            t[i] = ('N', -value)
        elif direction == 'W':
            t[i] = ('E', -value)
        elif direction in ('L', 'R'):
            facing = translate_turn(facing, direction, value)
            t[i] = ('N', 0)
        else:
            t[i] = (direction, value)
    pos = [0, 0]
    for i in t:
        direction, value = i
        if direction == 'N':
            pos[0] += value
        else:
            pos[1] += value
    print(sum(list(map(abs, pos))))