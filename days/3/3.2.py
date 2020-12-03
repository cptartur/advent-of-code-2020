from functools import reduce

with open(r'days\3\input.txt', 'r') as f:
    t = f.read().split()
    height = len(t)
    line_width = len(t[0])
    results = []
    steps = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    for step in steps:
        trees = 0
        i, j = 0, 0
        for i in range(0, height, step[1]):
            if t[i][j % line_width] == '#':
                trees += 1
            j += step[0]
        results.append(trees)
    print(reduce(lambda x, y: x * y, results))