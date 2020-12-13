from sympy.ntheory.modular import crt

with open(r'days\13\input.txt', 'r') as f:
    start, line = f.read().split()
    start = int(start)
    t = [(int(v), -i) for i, v in enumerate(line.split(',')) if str.isdigit(v)]
    m, v = zip(*t)
    print(crt(m, v)[0])