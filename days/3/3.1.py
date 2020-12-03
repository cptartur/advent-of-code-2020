with open(r'days\3\input.txt', 'r') as f:
    t = f.read().split()
    height = len(t)
    line_width = len(t[0])
    trees = 0
    i = 0
    for line in t:
        if line[i % line_width] == '#':
            trees += 1
        i += 3
    print(trees)
