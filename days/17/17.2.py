import itertools
import collections
import copy

def generate_neighbors(coords, point):
    n = set()
    for t in itertools.product((-1, 0, 1), repeat=4):
        t = tuple(map(sum, zip(t, point)))
        n.add(t)
    n.remove(point)
    return n

def evolve(coords):
    for _ in range(6):
        old_coords = copy.deepcopy(coords)
        counter = collections.Counter()
        for c in old_coords:
            neighbors = generate_neighbors(old_coords, c)
            counter.update(neighbors)
            count = 0
            for n in neighbors:
                if n in old_coords:
                    count += 1
            if count not in (2, 3):
                coords.remove(c)
        for key, count in counter.items():
            if count == 3:
                coords.add(key)
        old_coords = coords

with open(r'days\17\input.txt', 'r') as f:
    data = [i for i in f.read().split()]
    coords = {(x, y, 0, 0) for x, line in enumerate(data) for y, v in enumerate(line) if v == '#'}
    evolve(coords)
    print(len(coords))